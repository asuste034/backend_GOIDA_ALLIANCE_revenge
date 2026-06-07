from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user.services import UserRepository
from user.schemes import UserCreate
from db import get_db

user_router = APIRouter(prefix='/user', tags=['users'])

@user_router.get('/all')
async def get_all_users(
    session: AsyncSession = Depends(get_db)
    ):
    users = await UserRepository.get_all_users(session=session)
    return users

@user_router.post('/create')
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_db)
    ):
    user = await UserRepository.create_user(session=session, user=user)
    return user
