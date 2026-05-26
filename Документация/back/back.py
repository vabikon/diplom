from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
from datetime import datetime, timedelta
import uuid
import os
from sqlalchemy.orm import Session

# Import database modules
from database.database import engine, get_db
from models import models
from schemas import schemas
from crud import crud
from auth.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_current_admin_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

app = FastAPI(title="Ресторан Гастрономия API", version="1.0.0")

# Создаем директорию для хранения изображений
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем статические файлы для изображений
app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

# Корневой эндпоинт
@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API ресторана 'Гастрономия'",
        "version": "1.0.0",
        "endpoints": {
            "menu": "/api/menu",
            "reviews": "/api/reviews",
            "gallery": "/api/gallery",
            "orders": "/api/orders",
            "reservations": "/api/table-reservations",
            "auth": "/api/auth/login"
        }
    }

# АВТОРИЗАЦИЯ
@app.post("/api/auth/login", response_model=schemas.Token)
async def login(credentials: schemas.LoginRequest, db: Session = Depends(get_db)):
    """Вход в систему с получением JWT токена"""
    user = authenticate_user(db, credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/auth/verify", response_model=schemas.User)
async def verify_token(current_user: models.User = Depends(get_current_user)):
    """Проверка валидности токена и получение информации о пользователе"""
    return current_user


@app.get("/api/auth/me", response_model=schemas.User)
async def get_current_user_info(current_user: models.User = Depends(get_current_user)):
    """Получить информацию о текущем пользователе"""
    return current_user

# МЕНЮ
@app.get("/api/menu", response_model=List[schemas.MenuItem])
async def get_menu(category: Optional[str] = None, db: Session = Depends(get_db)):
    """Получить все блюда меню"""
    menu_items = crud.get_menu_items(db, category=category)
    return menu_items

@app.get("/api/menu/featured", response_model=List[schemas.MenuItem])
async def get_featured_menu(db: Session = Depends(get_db)):
    """Получить избранные блюда"""
    featured = crud.get_featured_menu_items(db)
    return featured

@app.get("/api/menu/{item_id}", response_model=schemas.MenuItem)
async def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    """Получить блюдо по ID"""
    db_item = crud.get_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Блюдо не найдено")
    return db_item

@app.post("/api/menu", response_model=schemas.MenuItem)
async def create_menu_item(
    item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Создать новое блюдо (требует авторизации администратора)"""
    return crud.create_menu_item(db=db, item=item)

@app.put("/api/menu/{item_id}", response_model=schemas.MenuItem)
async def update_menu_item(
    item_id: int,
    item: schemas.MenuItemUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить блюдо (требует авторизации администратора)"""
    db_item = crud.update_menu_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Блюдо не найдено")
    return db_item

@app.delete("/api/menu/{item_id}")
async def delete_menu_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Удалить блюдо (требует авторизации администратора)"""
    db_item = crud.delete_menu_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Блюдо не найдено")
    return {"message": "Блюдо удалено"}

# ОТЗЫВЫ
@app.get("/api/reviews", response_model=List[schemas.Review])
async def get_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить отзывы с возможностью пагинации"""
    reviews = crud.get_reviews(db, skip=skip, limit=limit)
    return reviews

@app.get("/api/reviews/{review_id}", response_model=schemas.Review)
async def get_review(review_id: int, db: Session = Depends(get_db)):
    """Получить отзыв по ID"""
    db_review = crud.get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    return db_review


@app.post("/api/reviews", response_model=schemas.Review)
async def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    """Создать новый отзыв"""
    return crud.create_review(db=db, review=review)

@app.put("/api/reviews/{review_id}", response_model=schemas.Review)
async def update_review(
    review_id: int,
    review: schemas.ReviewUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить отзыв (требует авторизации администратора)"""
    db_review = crud.update_review(db=db, review_id=review_id, review=review)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    return db_review

@app.delete("/api/reviews/{review_id}")
async def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Удалить отзыв (требует авторизации администратора)"""
    db_review = crud.delete_review(db=db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    return {"message": "Отзыв удален"}

@app.get("/api/reviews/stats")
async def get_reviews_stats(db: Session = Depends(get_db)):
    """Получить статистику по отзывам"""
    return crud.get_reviews_stats(db)

# ГАЛЕРЕЯ
@app.get("/api/gallery", response_model=List[schemas.GalleryImage])
async def get_gallery_paginated(category: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить изображения галереи с пагинацией"""
    gallery_images = crud.get_gallery_images(db, category=category, skip=skip, limit=limit)
    return gallery_images

@app.get("/api/gallery/{image_id}", response_model=schemas.GalleryImage)
async def get_gallery_image(image_id: int, db: Session = Depends(get_db)):
    """Получить изображение по ID"""
    db_image = crud.get_gallery_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Изображение не найдено")
    return db_image

@app.post("/api/gallery", response_model=schemas.GalleryImage)
async def create_gallery_image(
    image: schemas.GalleryImageCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Добавить новое изображение в галерею (требует авторизации администратора)"""
    return crud.create_gallery_image(db=db, image=image)

@app.put("/api/gallery/{image_id}", response_model=schemas.GalleryImage)
async def update_gallery_image(
    image_id: int,
    image: schemas.GalleryImageUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить изображение в галерее (требует авторизации администратора)"""
    db_image = crud.update_gallery_image(db=db, image_id=image_id, image=image)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Изображение не найдено")
    return db_image

@app.delete("/api/gallery/{image_id}")
async def delete_gallery_image(
    image_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Удалить изображение из галереи (требует авторизации администратора)"""
    db_image = crud.delete_gallery_image(db=db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Изображение не найдено")
    return {"message": "Изображение удалено"}

# ЗАКАЗЫ
@app.get("/api/orders", response_model=List[schemas.Order])
async def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить все заказы"""
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@app.get("/api/orders/{order_id}", response_model=schemas.Order)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    """Получить заказ по ID"""
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order

@app.post("/api/orders", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """Создать новый заказ"""
    db_order = crud.create_order(db=db, order=order)

    # Здесь можно добавить отправку email или уведомление администратору
    print(f"Новый заказ #{db_order.id} на сумму {db_order.total} руб.")

    return db_order

@app.put("/api/orders/{order_id}", response_model=schemas.Order)
async def update_order(
    order_id: int,
    order: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить заказ (требует авторизации администратора)"""
    db_order = crud.update_order(db=db, order_id=order_id, order=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order

@app.put("/api/orders/{order_id}/status", response_model=schemas.Order)
async def update_order_status(
    order_id: int,
    status_data: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить статус заказа (требует авторизации администратора)"""
    db_order = crud.update_order_status(db=db, order_id=order_id, status=status_data.status)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order

@app.delete("/api/orders/{order_id}")
async def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Удалить заказ (требует авторизации администратора)"""
    db_order = crud.delete_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return {"message": "Заказ удален"}

# Бронирование стола
@app.get("/api/table-reservations", response_model=List[schemas.TableReservation])
async def get_table_reservations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Получить все бронирования столов (требует авторизации администратора)"""
    return crud.get_table_reservations(db, skip=skip, limit=limit)


@app.get("/api/table-reservations/{reservation_id}", response_model=schemas.TableReservation)
async def get_table_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Получить бронирование стола по ID (требует авторизации администратора)"""
    db_reservation = crud.get_table_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return db_reservation


@app.post("/api/table-reservations", response_model=schemas.TableReservation)
async def create_reservation(
    reservation: schemas.TableReservationCreate,
    db: Session = Depends(get_db)
):
    """Создать бронирование стола"""
    db_reservation = crud.create_table_reservation(db=db, reservation=reservation)
    print(
        "Новое бронирование стола "
        f"#{db_reservation.id}: {db_reservation.customer_phone}"
    )
    return db_reservation


@app.put("/api/table-reservations/{reservation_id}/status", response_model=schemas.TableReservation)
async def update_table_reservation_status(
    reservation_id: int,
    status_data: schemas.TableReservationStatusUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Обновить статус бронирования стола (требует авторизации администратора)"""
    db_reservation = crud.update_table_reservation_status(
        db=db,
        reservation_id=reservation_id,
        status=status_data.status,
    )
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return db_reservation


@app.delete("/api/table-reservations/{reservation_id}")
async def delete_table_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Удалить бронирование стола (требует авторизации администратора)"""
    db_reservation = crud.delete_table_reservation(db=db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return {"message": "Бронирование удалено"}

# Поиск
@app.get("/api/search")
async def search(query: str, db: Session = Depends(get_db)):
    """Поиск по меню и отзывам"""
    return crud.search_menu_and_reviews(db, query)


# Загрузка изображений
@app.post("/api/upload-image")
async def upload_image(file: UploadFile = File(...)):
    """Загрузить изображение на сервер"""
    # Проверяем, что файл является изображением
    allowed_types = ["image/jpeg", "image/jpg", "image/png", "image/gif", "image/webp"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Недопустимый тип файла. Разрешены: JPEG, PNG, GIF, WEBP")

    # Генерируем уникальное имя файла
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(IMAGES_DIR, unique_filename)

    # Сохраняем файл
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Возвращаем URL для доступа к изображению
    return {
        "filename": unique_filename,
        "url": f"/images/{unique_filename}",
        "size": os.path.getsize(file_path),
        "content_type": file.content_type
    }

# Получение списка всех изображений
@app.get("/api/images")
async def list_images():
    """Получить список всех загруженных изображений"""
    image_files = []
    for filename in os.listdir(IMAGES_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            file_path = os.path.join(IMAGES_DIR, filename)
            image_files.append({
                "filename": filename,
                "url": f"/images/{filename}",
                "size": os.path.getsize(file_path),
                "created_at": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
            })

    return {"images": image_files}

# Получение информации о конкретном изображении
@app.get("/api/images/{filename}")
async def get_image_info(filename: str):
    """Получить информацию об изображении"""
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Изображение не найдено")

    return {
        "filename": filename,
        "url": f"/images/{filename}",
        "size": os.path.getsize(file_path),
        "content_type": get_content_type(file_path),
        "created_at": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
    }

# Вспомогательная функция для определения MIME-типа
def get_content_type(file_path):
    """Определить MIME-тип файла по расширению"""
    import mimetypes
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or "application/octet-stream"

# Тестовый эндпоинт для проверки
@app.get("/api/health")
async def health_check(db: Session = Depends(get_db)):
    """Проверка здоровья API"""
    # Получаем количество записей в каждой таблице
    menu_count = db.query(models.MenuItem).count()
    review_count = db.query(models.Review).count()
    gallery_count = db.query(models.GalleryImage).count()
    order_count = db.query(models.Order).count()
    reservation_count = db.query(models.TableReservation).count()

    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "counts": {
            "menu_items": menu_count,
            "reviews": review_count,
            "gallery_images": gallery_count,
            "orders": order_count,
            "table_reservations": reservation_count
        }
    }

if __name__ == "__main__":
    import uvicorn
    from database.init_db import init_db

    # Initialize the database with sample data
    init_db()

    uvicorn.run(app, host="0.0.0.0", port=3344)
