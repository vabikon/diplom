# Database initialization
from sqlalchemy.orm import Session
from models.models import MenuItem, Review, GalleryImage, Order, User
from sqlalchemy import create_engine
from database.database import Base, SessionLocal, engine
from auth.auth import get_password_hash
import uuid
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()


def init_db(seed_sample_data: bool = True):
    # Create tables
    Base.metadata.create_all(bind=engine)

    # Populate initial data
    db = SessionLocal()
    
    try:
        # Menu items
        menu_items_data = [
            {
                "name": "Брускетта с томатами",
                "category": "appetizers",
                "price": 450,
                "weight": 180,
                "composition": "Тост, свежие томаты, базилик, оливковое масло, чеснок",
                "description": "Итальянская закуска на поджаренном хлебе",
                "image": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=400&fit=crop&crop=center",
                "featured": True
            },
            {
                "name": "Салат Цезарь",
                "category": "appetizers",
                "price": 590,
                "weight": 250,
                "composition": "Куриное филе, салат айсберг, пармезан, гренки, соус цезарь",
                "description": "Классический салат с курицей и сыром пармезан",
                "image": "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&fit=crop&crop=center",
                "featured": True
            },
            {
                "name": "Стейк Рибай",
                "category": "main",
                "price": 1890,
                "weight": 350,
                "composition": "Мраморная говядина, розмарин, тимьян, овощи гриль",
                "description": "Премиальный стейк на кости",
                "image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400&fit=crop&crop=center",
                "featured": True
            },
            {
                "name": "Лосось в кунжутной корочке",
                "category": "main",
                "price": 1450,
                "weight": 280,
                "composition": "Филе лосося, кунжут, соевый соус, рис, овощи",
                "description": "Нежное филе лосося в хрустящей кунжутной корочке",
                "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&fit=crop&crop=center",
                "featured": True
            },
            {
                "name": "Паста Карбонара",
                "category": "main",
                "price": 850,
                "weight": 320,
                "composition": "Спагетти, бекон, яйцо, пармезан, черный перец",
                "description": "Классическая итальянская паста",
                "image": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400&fit=crop&crop=center",
                "featured": False
            },
            {
                "name": "Тирамису",
                "category": "desserts",
                "price": 650,
                "weight": 150,
                "composition": "Сыр маскарпоне, савоярди, кофе, какао, яйца",
                "description": "Классический итальянский десерт",
                "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400&fit=crop&crop=center",
                "featured": True
            },
            {
                "name": "Чизкейк Нью-Йорк",
                "category": "desserts",
                "price": 550,
                "weight": 180,
                "composition": "Сливочный сыр, песочная основа, ягоды, ваниль",
                "description": "Нежный сливочный чизкейк",
                "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=400&fit=crop&crop=center",
                "featured": False
            },
            {
                "name": "Мохито",
                "category": "drinks",
                "price": 450,
                "weight": 400,
                "composition": "Светлый ром, лайм, мята, сахар, содовая",
                "description": "Классический кубинский коктейль",
                "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=400&fit=crop&crop=center",
                "featured": False
            },
            {
                "name": "Капучино",
                "category": "drinks",
                "price": 320,
                "weight": 200,
                "composition": "Эспрессо, молоко, молочная пенка",
                "description": "Итальянский кофе с молочной пенкой",
                "image": "https://images.unsplash.com/photo-1561047029-3000c68339ca?w=400&fit=crop&crop=center",
                "featured": False
            }
        ]

        if seed_sample_data and db.query(MenuItem).count() == 0:
            for item_data in menu_items_data:
                menu_item = MenuItem(**item_data)
                db.add(menu_item)

        # Reviews
        reviews_data = [
            {
                "name": "Анна Петрова",
                "email": "anna@example.com",
                "rating": 5,
                "text": "Отличный ресторан! Вкусная еда и уютная атмосфера. Обязательно вернусь снова!",
                "date": datetime.fromisoformat("2024-01-15T00:00:00"),
                "answer": "Анна, спасибо за ваш отзыв! Ждем вас снова!"
            },
            {
                "name": "Иван Сидоров",
                "email": "ivan@example.com",
                "rating": 4,
                "text": "Хорошее место для семейного ужина. Особенно понравились горячие блюда.",
                "date": datetime.fromisoformat("2024-01-10T00:00:00"),
                "answer": "Иван, рады, что вам понравилось!"
            },
            {
                "name": "Мария Иванова",
                "rating": 5,
                "text": "Лучший стейк в городе! Отличное обслуживание и атмосфера.",
                "date": datetime.fromisoformat("2024-01-05T00:00:00"),
                "answer": "Мария, благодарим за высокую оценку!"
            },
            {
                "name": "Дмитрий Кузнецов",
                "rating": 5,
                "text": "Отмечали здесь день рождения. Все было идеально!",
                "date": datetime.fromisoformat("2024-01-01T00:00:00"),
                "answer": "Дмитрий, рады были сделать ваш праздник особенным!"
            }
        ]

        if seed_sample_data and db.query(Review).count() == 0:
            for review_data in reviews_data:
                review = Review(**review_data)
                db.add(review)

        # Gallery images
        gallery_images_data = [
            {
                "src": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&fit=crop&crop=center",
                "alt": "Интерьер зала",
                "description": "Просторный зал с панорамными окнами",
                "category": "interior"
            },
            {
                "src": "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?w=800&fit=crop&crop=center",
                "alt": "Открытая кухня",
                "description": "Шеф-повар за работой на открытой кухне",
                "category": "interior"
            },
            {
                "src": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&fit=crop&crop=center",
                "alt": "Подача блюд",
                "description": "Искусство сервировки наших блюд",
                "category": "food"
            },
            {
                "src": "https://images.unsplash.com/photo-1554679665-f5537f187268?w=800&fit=crop&crop=center",
                "alt": "Барная стойка",
                "description": "Бар с авторскими коктейлями",
                "category": "interior"
            },
            {
                "src": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800&fit=crop&crop=center",
                "alt": "Летняя терраса",
                "description": "Терраса с видом на парк",
                "category": "interior"
            },
            {
                "src": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=800&fit=crop&crop=center",
                "alt": "Банкетный зал",
                "description": "Зал для торжественных мероприятий",
                "category": "events"
            },
            {
                "src": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&fit=crop&crop=center",
                "alt": "Готовим стейк",
                "description": "Приготовление стейка на открытом огне",
                "category": "food"
            },
            {
                "src": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&fit=crop&crop=center",
                "alt": "Ужин при свечах",
                "description": "Романтический ужин в нашем ресторане",
                "category": "interior"
            }
        ]

        if seed_sample_data and db.query(GalleryImage).count() == 0:
            for image_data in gallery_images_data:
                image = GalleryImage(**image_data)
                db.add(image)

        # Create default admin user
        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        admin_email = os.getenv("ADMIN_EMAIL", "admin@restaurant.com")
        existing_admin = db.query(User).filter(User.username == admin_username).first()
        if existing_admin is None:
            admin_user = User(
                username=admin_username,
                email=admin_email,
                hashed_password=get_password_hash(admin_password),
                is_active=True,
                is_admin=True,
            )
            db.add(admin_user)

        db.commit()
        if seed_sample_data:
            print("Database checked and sample data ensured")
        print(f"Admin user ensured: username='{admin_username}'")

    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()
