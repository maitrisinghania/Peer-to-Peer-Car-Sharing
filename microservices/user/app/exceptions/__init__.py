from fastapi import HTTPException

class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="User not found")

class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Unauthenticated")

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=403, detail=detail)