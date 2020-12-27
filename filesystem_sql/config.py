import os


PGSQL_DB = os.environ.get("PGSQL_DB", "filesystem_sql")
PGSQL_HOST = os.environ.get("PGSQL_HOST", "db_filesystem_sql")
PGSQL_PASS = os.environ.get("PGSQL_PASS", "filesystem_sql")
PGSQL_USR = os.environ.get("PGSQL_USR", "filesystem_sql")
PGSQL_PORT = os.environ.get("PGSQL_PORT", "5432")
