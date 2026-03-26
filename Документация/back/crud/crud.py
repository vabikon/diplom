# CRUD operations
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.models import MenuItem, Review, GalleryImage, Order, TableReservation, User
from schemas import schemas
from auth.auth import get_password_hash
import json
from fastapi import HTTPException

# Constants
VALID_ORDER_STATUSES = ["pending", "confirmed", "preparing", "ready", "delivered", "cancelled"]
VALID_RESERVATION_STATUSES = ["pending", "confirmed", "completed", "cancelled"]


# MenuItem CRUD operations
def get_menu_item(db: Session, item_id: int):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    return db_item


def get_menu_items(db: Session, category: str = None, skip: int = 0, limit: int = 100):
    query = db.query(MenuItem)
    if category:
        query = query.filter(MenuItem.category == category)
    return query.offset(skip).limit(limit).all()


def get_featured_menu_items(db: Session):
    return db.query(MenuItem).filter(MenuItem.featured == True).all()


def create_menu_item(db: Session, item: schemas.MenuItemCreate):
    db_item = MenuItem(**item.dict())
    try:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating menu item: {str(e)}")


def update_menu_item(db: Session, item_id: int, item: schemas.MenuItemUpdate):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not db_item:
        return None

    try:
        update_data = item.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating menu item: {str(e)}")


def delete_menu_item(db: Session, item_id: int):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not db_item:
        return None

    try:
        db.delete(db_item)
        db.commit()
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting menu item: {str(e)}")


# Review CRUD operations
def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Review).order_by(Review.id.desc()).offset(skip).limit(limit).all()


def create_review(db: Session, review: schemas.ReviewCreate):
    # Validate rating range
    if review.rating < 1 or review.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")

    db_review = Review(**review.dict())
    try:
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating review: {str(e)}")


def update_review(db: Session, review_id: int, review: schemas.ReviewUpdate):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        return None

    # Validate rating range if provided
    if review.rating is not None and (review.rating < 1 or review.rating > 5):
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")

    try:
        update_data = review.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_review, field, value)
        db.commit()
        db.refresh(db_review)
        return db_review
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating review: {str(e)}")


def delete_review(db: Session, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        return None

    try:
        db.delete(db_review)
        db.commit()
        return db_review
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting review: {str(e)}")


def get_reviews_stats(db: Session):
    reviews = db.query(Review).all()
    if not reviews:
        return {"count": 0, "average_rating": 0}

    total_rating = sum(review.rating for review in reviews)
    average_rating = total_rating / len(reviews)

    return {
        "count": len(reviews),
        "average_rating": round(average_rating, 1)
    }


# GalleryImage CRUD operations
def get_gallery_image(db: Session, image_id: int):
    return db.query(GalleryImage).filter(GalleryImage.id == image_id).first()


def get_gallery_images(db: Session, category: str = None, skip: int = 0, limit: int = 100):
    query = db.query(GalleryImage)
    if category:
        query = query.filter(GalleryImage.category == category)
    return query.offset(skip).limit(limit).all()


def create_gallery_image(db: Session, image: schemas.GalleryImageCreate):
    db_image = GalleryImage(**image.dict())
    try:
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating gallery image: {str(e)}")


def update_gallery_image(db: Session, image_id: int, image: schemas.GalleryImageUpdate):
    db_image = db.query(GalleryImage).filter(GalleryImage.id == image_id).first()
    if not db_image:
        return None

    try:
        update_data = image.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_image, field, value)
        db.commit()
        db.refresh(db_image)
        return db_image
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating gallery image: {str(e)}")


def delete_gallery_image(db: Session, image_id: int):
    db_image = db.query(GalleryImage).filter(GalleryImage.id == image_id).first()
    if not db_image:
        return None

    try:
        db.delete(db_image)
        db.commit()
        return db_image
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting gallery image: {str(e)}")


# Order CRUD operations
def get_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        # Преобразуем JSON-строку в объект Python
        import json
        if isinstance(db_order.items, str):
            try:
                db_order.items = json.loads(db_order.items)
            except json.JSONDecodeError:
                db_order.items = []
    return db_order


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    orders = db.query(Order).offset(skip).limit(limit).all()
    # Преобразуем JSON-строки в объекты Python
    import json
    for order in orders:
        if isinstance(order.items, str):
            try:
                order.items = json.loads(order.items)
            except json.JSONDecodeError:
                order.items = []
    return orders


def create_order(db: Session, order: schemas.OrderCreate):
    # Validate required fields
    if not order.customer_phone:
        raise HTTPException(status_code=400, detail="Customer phone is required")

    # Convert items list to JSON string for storage
    try:
        items_json = json.dumps(order.items)
        db_order = Order(
            items=items_json,
            total=order.total,
            customer_name=order.customer_name or "Гость",
            customer_phone=order.customer_phone,
            customer_email=order.customer_email,
            address=order.address,
            status=order.status
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating order: {str(e)}")


def update_order(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None

    try:
        update_data = order.dict(exclude_unset=True)
        # Handle items separately since it's stored as JSON
        if "items" in update_data:
            items_json = json.dumps(update_data.pop("items"))
            db_order.items = items_json
        for field, value in update_data.items():
            setattr(db_order, field, value)
        db.commit()
        db.refresh(db_order)

        # Преобразуем JSON-строку в объект Python перед возвратом
        if isinstance(db_order.items, str):
            try:
                db_order.items = json.loads(db_order.items)
            except json.JSONDecodeError:
                db_order.items = []

        return db_order
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating order: {str(e)}")


def update_order_status(db: Session, order_id: int, status: str):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None

    # Validate status
    if status not in VALID_ORDER_STATUSES:
        raise HTTPException(status_code=400, detail=f"Invalid status. Valid statuses are: {VALID_ORDER_STATUSES}")

    try:
        db_order.status = status
        db.commit()
        db.refresh(db_order)

        # Преобразуем JSON-строку в объект Python перед возвратом
        if isinstance(db_order.items, str):
            try:
                db_order.items = json.loads(db_order.items)
            except json.JSONDecodeError:
                db_order.items = []

        return db_order
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating order status: {str(e)}")


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None

    # Преобразуем JSON-строку в объект Python перед возвратом
    if isinstance(db_order.items, str):
        try:
            import json
            db_order.items = json.loads(db_order.items)
        except json.JSONDecodeError:
            db_order.items = []

    try:
        db.delete(db_order)
        db.commit()
        return db_order
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting order: {str(e)}")


# Table reservation CRUD operations
def get_table_reservation(db: Session, reservation_id: int):
    return db.query(TableReservation).filter(TableReservation.id == reservation_id).first()


def get_table_reservations(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(TableReservation)
        .order_by(TableReservation.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_table_reservation(db: Session, reservation: schemas.TableReservationCreate):
    if not reservation.customer_phone:
        raise HTTPException(status_code=400, detail="Customer phone is required")

    db_reservation = TableReservation(
        customer_phone=reservation.customer_phone,
        reservation_type=reservation.reservation_type,
        source=reservation.source,
        status="pending",
    )

    try:
        db.add(db_reservation)
        db.commit()
        db.refresh(db_reservation)
        return db_reservation
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error creating table reservation: {str(e)}",
        )


def update_table_reservation_status(db: Session, reservation_id: int, status: str):
    db_reservation = (
        db.query(TableReservation).filter(TableReservation.id == reservation_id).first()
    )
    if not db_reservation:
        return None

    if status not in VALID_RESERVATION_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status. Valid statuses are: {VALID_RESERVATION_STATUSES}",
        )

    try:
        db_reservation.status = status
        db.commit()
        db.refresh(db_reservation)
        return db_reservation
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error updating table reservation status: {str(e)}",
        )


def delete_table_reservation(db: Session, reservation_id: int):
    db_reservation = (
        db.query(TableReservation).filter(TableReservation.id == reservation_id).first()
    )
    if not db_reservation:
        return None

    try:
        db.delete(db_reservation)
        db.commit()
        return db_reservation
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error deleting table reservation: {str(e)}",
        )


# Search functionality
def search_menu_and_reviews(db: Session, query: str):
    if not query:
        return {"menu": [], "reviews": []}

    query_lower = query.lower()

    try:
        # Search in menu items
        menu_results = db.query(MenuItem).filter(
            or_(
                MenuItem.name.contains(query_lower),
                MenuItem.description.contains(query_lower),
                MenuItem.composition.contains(query_lower)
            )
        ).all()

        # Search in reviews
        review_results = db.query(Review).filter(
            or_(
                Review.name.contains(query_lower),
                Review.text.contains(query_lower)
            )
        ).order_by(Review.id.desc()).all()

        return {
            "menu": menu_results,
            "reviews": review_results
        }
    except Exception as e:
        # Log the error for debugging
        print(f"Search error: {str(e)}")
        # Return empty results in case of error
        return {"menu": [], "reviews": []}


# User CRUD operations
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # Check if user already exists
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    existing_email = get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    try:
        update_data = user.dict(exclude_unset=True)
        # Handle password separately
        if "password" in update_data:
            hashed_password = get_password_hash(update_data.pop("password"))
            db_user.hashed_password = hashed_password

        for field, value in update_data.items():
            setattr(db_user, field, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating user: {str(e)}")


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    try:
        db.delete(db_user)
        db.commit()
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting user: {str(e)}")
