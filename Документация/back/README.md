## Быстрый старт

1. Установи зависимости  
   ```bash
   pip install -r requirements.txt
   ```

2. Создай файл `.env` в корне проекта и вставь в него:

   ```env
   # Database
   DATABASE_URL=sqlite:///./restaurant.db

   # JWT Configuration
   SECRET_KEY=9f3c8a7e6d5b4a3c2e1f0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4e3d2c1b0a9f
   ACCESS_TOKEN_EXPIRE_MINUTES=1440

   # Admin User Configuration
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=admin123
   ADMIN_EMAIL=admin@restaurant.com

   # CORS Configuration (для продакшена укажите конкретный домен вместо *)
   # ALLOWED_ORIGINS=http://localhost:5173,https://your-frontend-domain.com
   ALLOWED_ORIGINS=*
   ```

3. Запусти сервер

   ```bash
   python back.py
   ```

   или (если используешь uvicorn напрямую):

   ```bash
   uvicorn back:app --reload
   ```

→ Документация API будет доступна здесь:  
http://127.0.0.1:8000/docs  
http://127.0.0.1:8000/redoc

## Основные команды

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск с авто-перезагрузкой 
uvicorn back:app --reload

# Запуск обычный (для продакшена / тестов)
python back.py
# или
uvicorn back:app --host 0.0.0.0 --port 8000
```
