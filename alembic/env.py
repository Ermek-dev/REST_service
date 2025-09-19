import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# путь к проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# импортируем Base и URL
from app.db import Base, DATABASE_URL_SYNC
import app.models  # подтягиваем все модели

config = context.config

# эскейпим символы % в пароле
config.set_main_option("sqlalchemy.url", DATABASE_URL_SYNC.replace("%", "%%"))

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# --- остальной стандартный код Alembic для run_migrations_online/run_migrations_offline ---

