import os.path

DEBUG = True

# SAE storage domain name.
STORAGE_DOMAIN = 'thunder'

# Database Configuration.
if DEBUG:
    MYSQL_DB = "thunder"
    MYSQL_USER = 'root'
    MYSQL_PASS = "collegetime"
    MYSQL_HOST_M = MYSQL_HOST_S = 'localhost'
    MYSQL_PORT = 3306
else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT

MAX_IDLE_TIME = 5

# Upload Path.
# UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'uploads/')
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), '/static/uploads/')

# Pagination
ITEMS_PER_PAGE = 15
