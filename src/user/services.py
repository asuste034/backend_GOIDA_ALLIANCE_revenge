from sqlalchemy import select
from models import User
from user.schemes import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    @classmethod
    async def create_user(cls, 
                          session: AsyncSession,
                          user: UserCreate) -> User:
        async with session.begin():
            new_user = User(**user.model_dump())
            session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

    @classmethod
    async def get_all_users(cls,
                            session: AsyncSession) -> list[User]:
        result = await session.execute(select(User))
        return result.scalars().all()
    
    @classmethod
    async def get_user_by_id(cls,
                             session: AsyncSession,
                             user_id: int) -> User | None:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()
    
    @classmethod
    async def get_user_by_username(cls,
                                   session: AsyncSession,
                                   username: str) -> User | None:
        result = await session.execute(select(User).where(User.name == username))
        return result.scalars().first()
    
    @classmethod
    async def delete_user(cls,
                              session: AsyncSession,
                              user_id: int) -> bool:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            return False
        await session.delete(user)
        await session.commit()
        return True