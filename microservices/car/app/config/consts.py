## Routes
PATH_PREFIX_CAR = "/cars"

# Car Routes
class CarRoutes:
    POST_ADD_CAR = "/add_car"
    
    PUT_DEACTIVATE_CARS = "/deactivate_cars"
    PUT_RECOVER_CARS = "/recover_cars"
    PUT_CAR_ADDED_IN_TRANS = "/car_add_in_transaction"
    PUT_CAR_ROLLBACK_IN_TRANS = "/car_rollback_in_transaction"

    GET_ALL_CARS = "/get_all_cars"
    GET_CAR = "/get_car"
    GET_CARS_LIST = "/get_cars_list"
    GET_DELETED_CARS = "/get_deleted_cars"

    DELETE_CARS = "/delete_cars"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imscar"

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "ID not found"
ACTIVE_ID_NOT_FOUND = "Active ID not found"
NAME_NOT_FOUND = "Name not found"
USED_IN_TRANSACTION_NOT_FOUND = "usedInTransaction not found"
INVALID_CAR_DETAILS_TYPE = "Invalid car details type"
CAR_DETAILS_MISSING = "Car details are missing"
CAR_DOES_NOT_EXIST = "Car does not exist"
CANNOT_BE_USED_IN_TRANSACTION = "Cannot be used in transaction"
CANNOT_BE_ROLLBACKED_IN_TRANSACTION = "Cannot be rolled back in transaction"

# MODEL
ORG = "org"