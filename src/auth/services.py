from fastapi import HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.utils import create_access_token
from auth.schemes import Token, UserLogin
from user.services import UserRepository

class AuthService:
    @classmethod
    async def login_user(cls,
                         session: AsyncSession,
                         user: UserLogin) -> Token:
        user = await UserRepository.get_user_by_username(session, user.name)
        if user:
            token = create_access_token({"sub": str(user.id)})
            return Token(access_token=token)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="В")
        