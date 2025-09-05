import logging

from yoyo import get_backend, read_migrations

import backend.conf as conf

logger = logging.getLogger(__name__)
MIGRATIONS_PATH = "./backend/migrations"


def apply():
    backend = get_backend(conf.DATABASE_DSN)
    migrations = read_migrations(MIGRATIONS_PATH)
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
