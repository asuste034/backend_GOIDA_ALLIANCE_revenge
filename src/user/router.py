from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user.services import UserRepository
from user.schemes import UserCreate
from db import get_db

auth_router = APIRouter(prefix='/user', tags=['users'])

@auth_router.post('/create')
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_db)
    ):
    user = await UserRepository.create_user(session=session, user=user)
    return user