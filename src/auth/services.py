from fastapi import HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.utils import create_access_token
from auth.schemes import Token, UserLogin
from user.services import UserRepository
from utils import verify_password

class AuthService:
    @classmethod
    async def login_user(cls,
                         session: AsyncSession,
                         user: UserLogin) -> Token:
        Userdb = await UserRepository.get_user_by_username(session, user.name)
        if Userdb and verify_password(user.password, Userdb.password):
            token = create_access_token({"sub": str(Userdb.id)})
            return Token(access_token=token)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="В")
        