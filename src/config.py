import os

DEBUG = False
# frozenset: a set that can't change
ADMINS = frozenset([
    os.environ.get("ADMIN_EMAIL")
])
END_POINT = "http://127.0.0.1:4990"