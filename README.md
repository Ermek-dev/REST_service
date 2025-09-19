Создание проекта FastAPI

# FastAPI Task Service

## Описание проекта
Небольшой REST-сервис на Python с использованием FastAPI для работы с задачами (Task).  
Сервис хранит данные в Supabase (Postgres), предоставляет CRUD-эндпоинты и полностью документирован через OpenAPI (Swagger UI).  

**Функциональность:**
- Создание, чтение, обновление и удаление задач
- Фильтрация задач по статусу
- Пагинация списка задач
- Проверка работоспособности сервиса через `/health`

**Нефункциональные требования:**
- Язык: Python 3.11+
- Фреймворк: FastAPI
- База данных: Supabase (Postgres)
- Контейнеризация: Docker + docker-compose
- Стиль разработки: GitFlow (ветки main, develop, feature/task)
- Документация: OpenAPI (Swagger UI) + README.md

---

## Сущность Task
| Поле         | Тип        | Обязательное | Описание                                    |
|--------------|-----------|--------------|--------------------------------------------|
| id           | int       | PK           | Уникальный идентификатор задачи            |
| title        | str       | Да           | Заголовок задачи                            |
| description  | str       | Нет          | Описание задачи                             |
| status       | str       | Нет          | Статус задачи: `todo`, `in_progress`, `done` (по умолчанию `todo`) |
| created_at   | datetime  | Нет          | Дата и время создания задачи (по умолчанию текущий момент) |

---

## Эндпоинты API

| Метод | URL              | Описание                                    |
|-------|-----------------|--------------------------------------------|
| POST  | `/tasks`         | Создать задачу                              |
| GET   | `/tasks`         | Получить список задач с пагинацией и фильтром по `status` |
| GET   | `/tasks/{id}`    | Получить задачу по ID                        |
| PUT   | `/tasks/{id}`    | Обновить задачу                              |
| DELETE| `/tasks/{id}`    | Удалить задачу                               |
| GET   | `/health`        | Проверка работоспособности сервиса `{ "status": "ok" }` |

Swagger UI доступен по адресу:  
http://localhost:8000/docs

yaml
Copy code

---

## Примеры запросов

**Создание задачи:**

curl -X POST "http://localhost:8000/tasks" \
-H "Content-Type: application/json" \
-d '{"title": "Новая задача", "description": "Описание задачи"}'
Получение списка задач с фильтром и пагинацией:


curl "http://localhost:8000/tasks?skip=0&limit=10&status=todo"
Обновление задачи:

curl -X PUT "http://localhost:8000/tasks/1" \
-H "Content-Type: application/json" \
-d '{"status": "in_progress"}'
Удаление задачи:

curl -X DELETE "http://localhost:8000/tasks/1"
Проверка состояния сервиса:
curl "http://localhost:8000/health"
Запуск проекта
Локально через uvicorn
Установить зависимости:


pip install -r requirements.txt
Создать .env на основе .env.example:

env

DATABASE_URL=postgresql+asyncpg://postgres:<PASSWORD>@db:5432/postgres
DATABASE_URL_SYNC=postgresql+psycopg2://postgres:<PASSWORD>@db:5432/postgres
Запустить приложение:
uvicorn app.main:app --reload
Через Docker
Собрать контейнеры и запустить сервис:

docker-compose up --build
Swagger UI доступен на:
http://localhost:8000/docs
Миграции базы данных
Используется Alembic.
Применить миграции:
docker exec -it fastapi_app alembic upgrade head
Подключение к Supabase
Создать проект в Supabase.

Получить данные для подключения: хост, порт, имя пользователя, пароль, имя базы данных.

Сохранить в .env:

env
DATABASE_URL=postgresql+asyncpg://<USER>:<PASSWORD>@<HOST>:5432/<DB_NAME>
DATABASE_URL_SYNC=postgresql+psycopg2://<USER>:<PASSWORD>@<HOST>:5432/<DB_NAME>
GitFlow
Ветка main — стабильная версия

Ветка develop — разработка и интеграция фич


Swagger UI доступен по адресу:  
