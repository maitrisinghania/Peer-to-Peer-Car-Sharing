## Routes
PATH_PREFIX_USER = "/users"

# User Routes
class UserRoutes:
    POST_ADD_USER = "/add_user"
    
    PUT_DEACTIVATE_USERS = "/deactivate_users"
    PUT_RECOVER_USERS = "/recover_users"
    PUT_USER_ADDED_IN_TRANS = "/user_add_in_transaction"
    PUT_USER_ROLLBACK_IN_TRANS = "/user_rollback_in_transaction"

    GET_ALL_USERS = "/get_all_users"
    GET_USER = "/get_user"
    GET_USERS_LIST = "/get_users_list"
    GET_DELETED_USERS = "/get_deleted_users"

    DELETE_USERS = "/delete_users"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imsuser"

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "ID not found"
ACTIVE_ID_NOT_FOUND = "Active ID not found"
NAME_NOT_FOUND = "Name not found"
USED_IN_TRANSACTION_NOT_FOUND = "usedInTransaction not found"
INVALID_USER_DETAILS_TYPE = "Invalid user details type"
USER_DETAILS_MISSING = "User details are missing"
USER_DOES_NOT_EXIST = "User does not exist"
CANNOT_BE_USED_IN_TRANSACTION = "Cannot be used in transaction"
CANNOT_BE_ROLLBACKED_IN_TRANSACTION = "Cannot be rolled back in transaction"

# MODEL
ORG = "org"