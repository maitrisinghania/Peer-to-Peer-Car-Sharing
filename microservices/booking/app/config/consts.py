## Routes
PATH_PREFIX_BOOKING = "/bookings"

# Booking Routes
class BookingRoutes:
    POST_ADD_BOOKING = "/add_booking"
    
    PUT_DEACTIVATE_BOOKINGS = "/deactivate_bookings"
    PUT_RECOVER_BOOKINGS = "/recover_bookings"
    PUT_BOOKING_ADDED_IN_TRANS = "/booking_add_in_transaction"
    PUT_BOOKING_ROLLBACK_IN_TRANS = "/booking_rollback_in_transaction"

    GET_ALL_BOOKINGS = "/get_all_bookings"
    GET_BOOKING = "/get_booking"
    GET_BOOKINGS_LIST = "/get_bookings_list"
    GET_DELETED_BOOKINGS = "/get_deleted_bookings"

    DELETE_BOOKINGS = "/delete_bookings"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imsbooking"

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "ID not found"
ACTIVE_ID_NOT_FOUND = "Active ID not found"
NAME_NOT_FOUND = "Name not found"
USED_IN_TRANSACTION_NOT_FOUND = "usedInTransaction not found"
INVALID_BOOKING_DETAILS_TYPE = "Invalid booking details type"
BOOKING_DETAILS_MISSING = "Booking details are missing"
BOOKING_DOES_NOT_EXIST = "Booking does not exist"
CANNOT_BE_USED_IN_TRANSACTION = "Cannot be used in transaction"
CANNOT_BE_ROLLBACKED_IN_TRANSACTION = "Cannot be rolled back in transaction"

# MODEL
ORG = "org"