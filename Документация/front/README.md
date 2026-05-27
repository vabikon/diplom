# Frontend

## Локальный запуск

1. Установи зависимости:
   ```bash
   npm install
   ```

2. Создай файл `.env` на основе `.env.example`.

3. Запусти dev-сервер:
   ```bash
   npm run dev
   ```

По умолчанию Vite откроет приложение на `http://localhost:5173`.

## Production

Для production-сборки уже подготовлен файл `.env.production` с относительными путями `/api` и `/api/auth`, чтобы фронтенд корректно работал за Nginx-прокси.

Сборка:

```bash
npm run build
```

