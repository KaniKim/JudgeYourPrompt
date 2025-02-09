from logging.config import fileConfig
import os

from dotenv import load_dotenv
from sqlalchemy import Connection, engine_from_config, text, pool

from alembic import context

__all__ = ["has_migration_been_applied"]

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

if not config.get_main_option("sqlalchemy.url"):
    load_dotenv()

    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    host = os.environ.get("DB_HOST")
    database = os.environ.get("DB_NAME")
    port = os.environ.get("DB_PORT")
    config.set_main_option(
        "sqlalchemy.url",
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}",
    )
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:

    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def has_migration_been_applied(connection: Connection, revision_id):
    # Query the alembic_version table to see if the given revision has been applied
    result = connection.execute(
        text(
            f"SELECT version_num FROM alembic_version WHERE version_num = {revision_id}",
        )
    )
    return result.fetchone() is not None


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema="alembic_version",
        )
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS alembic_version"))
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
