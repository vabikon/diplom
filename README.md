# Гастрономия

Полнофункциональное веб-приложение ресторана на `Vue 3 + FastAPI + SQLite + Docker`.

## Что уже готово для хостинга

- production-сборка фронтенда через `Документация/front/Dockerfile`
- backend-контейнер на `FastAPI`
- проксирование `/api` и `/images` через `Nginx`
- автоматическая инициализация пустой базы данных
- отдельные Docker volumes для БД и загруженных изображений
- шаблоны переменных окружения без локальных секретов

## Как опубликовать проект

1. Склонируй репозиторий на сервер.
2. Создай файл `.env` рядом с `docker-compose.yml`:
   ```bash
   cp .env.example .env
   ```
3. Обязательно измени в `.env`:
   - `SECRET_KEY`
   - `ADMIN_PASSWORD`
   - `ADMIN_EMAIL`
   - `ALLOWED_ORIGINS` на адрес вашего домена
4. Подними проект:
   ```bash
   docker compose up -d --build
   ```
5. Проверь здоровье API:
   ```bash
   curl http://localhost:3000/api/health
   ```

Сайт будет доступен на `http://localhost:3000` или на порту из `FRONTEND_PORT`.

## Структура

- `Документация/front` — Vue frontend
- `Документация/back` — FastAPI backend
- `docker-compose.yml` — основной способ запуска для хостинга

## Важно

- Локальные `.env`, `node_modules`, `dist`, `docker-data` и IDE-файлы в git не отправляются.
- Для первого старта demo-данные создаются автоматически, если база пустая и `INIT_SAMPLE_DATA=true`.
