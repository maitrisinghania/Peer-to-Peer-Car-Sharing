from fastapi import APIRouter, Query
from fastapi import Depends, Security

from typing import Dict, List, Optional

from ..config import logger
from ..config.consts import PATH_PREFIX_USER, UserRoutes, ORG

from ..models.user import User, ExceptionClass

from ..service import CreateUserService, ReadUserService, UpdateUserService, DeleteUserService

from ..utils import VerifyToken, UserValidators, set_org_model, set_org_multiple_model

apiRouter = APIRouter(prefix=PATH_PREFIX_USER)
auth = VerifyToken()

bad_request_responses = {
    400: {
        "description": "Error: Bad Request",
        "model": ExceptionClass
    }
}

auth_responses = {
    401: {
        "description": "Error: Unauthorized",
        "model": ExceptionClass
    },
    403: {
        "description": "Error: Forbidden",
        "model": ExceptionClass
    }
}

@apiRouter.post(UserRoutes.POST_ADD_USER, response_model=User, responses=bad_request_responses | auth_responses)
async def add_user(user: User = Depends(UserValidators.add_validator), auth_result: Dict = Security(auth.verify)) -> User:
    set_org_model(user, auth_result)
    logger.debug("In add_user:" + str(user))
    return CreateUserService.add_user(user)

@apiRouter.put(UserRoutes.PUT_DEACTIVATE_USERS, response_model=List[User], responses=auth_responses)
async def deactivate_users(users: List[User] = Depends(UserValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[User]:
    set_org_multiple_model(users, auth_result)
    logger.debug("In deactivate_users:" + str(users))
    UpdateUserService.deactivate_users(users)
    return await get_all_users(auth_result)

@apiRouter.put(UserRoutes.PUT_RECOVER_USERS, response_model=List[User], responses=auth_responses)
async def recover_users(users: List[User] = Depends(UserValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[User]:
    set_org_multiple_model(users, auth_result)
    logger.debug("In recover_users:" + str(users))
    UpdateUserService.recover_users(users)
    return await get_deleted_users(auth_result)

@apiRouter.put(UserRoutes.PUT_USER_ADDED_IN_TRANS, response_model=User, responses=bad_request_responses | auth_responses)
async def user_added_in_trans(user: User = Depends(UserValidators.id_validator), auth_result: Dict = Security(auth.verify)) -> User:
    set_org_model(user, auth_result)
    logger.debug("In user_added_in_trans:" + str(user))
    return UpdateUserService.user_in_transaction(user)

@apiRouter.put(UserRoutes.PUT_USER_ROLLBACK_IN_TRANS, response_model=User, responses=bad_request_responses | auth_responses)
async def rollback_added_in_trans(user: User = Depends(UserValidators.rollback_validator), auth_result: Dict = Security(auth.verify)) -> User:
    set_org_model(user, auth_result)
    logger.debug("In rollback_added_in_trans:" + str(user))
    return UpdateUserService.user_rollback_in_trans(user)

@apiRouter.get(UserRoutes.GET_USER + "/{user_id}", response_model=User, responses=bad_request_responses | auth_responses)
async def get_user(user_id: int, auth_result: Dict = Security(auth.verify)) -> User:
    user : User = User(id = user_id)
    set_org_model(user, auth_result)
    logger.debug("In get_user:" + str(user))
    return ReadUserService.get_user(user)

@apiRouter.get(UserRoutes.GET_ALL_USERS, response_model=List[User], responses=auth_responses)
async def get_all_users(auth_result: Dict = Security(auth.verify)) -> List[User]:
    user : User = set_org_model(User(), auth_result)
    logger.debug("In get_all_users:" + str(user))
    return ReadUserService.get_all_users(user)

@apiRouter.get(UserRoutes.GET_USERS_LIST+"/", response_model=List[Optional[User]], responses=auth_responses)
async def get_users_list(user_id: List[int] = Query([]), auth_result: Dict = Security(auth.verify)) -> List[Optional[User]]:
    logger.debug("In get_users_list:" + str(user_id))
    return ReadUserService.get_users_list(auth_result[ORG], user_id)

@apiRouter.get(UserRoutes.GET_DELETED_USERS, response_model=List[User], responses=auth_responses)
async def get_deleted_users(auth_result: Dict = Security(auth.verify)) -> List[User]:
    user : User = set_org_model(User(), auth_result)
    logger.debug("In get_deleted_users:" + str(user))
    return ReadUserService.get_deleted_users(user)

@apiRouter.delete(UserRoutes.DELETE_USERS, response_model=List[User], responses=auth_responses)
async def delete_users(users: List[User] = Depends(UserValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[User]:
    set_org_multiple_model(users, auth_result)
    logger.debug("In delete_users:" + str(users))
    DeleteUserService.delete_users(users)
    return await get_deleted_users(auth_result)