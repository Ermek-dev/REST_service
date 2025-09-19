import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Добавляем путь к проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем Base и модели
from app.db import Base, DATABASE_URL_SYNC
import app.models  # чтобы Alembic увидел все модели

# Alembic Config объект
config = context.config

# Подставляем URL для синхронного подключения
config.set_main_option("sqlalchemy.url", DATABASE_URL_SYNC.replace("%", "%%"))

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata всех моделей
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()



# --- остальной стандартный код Alembic для run_migrations_online/run_migrations_offline ---

