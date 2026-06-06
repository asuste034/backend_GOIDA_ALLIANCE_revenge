from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from event.schemes import Event
from models import EventBase


async def create_event(db: AsyncSession, event: Event):
    db_event = EventBase(**event.model_dump())
    db.add(db_event)
    await db.flush()
    await db.commit()
    await db.refresh(db_event)
    return db_event

async def delete_event(db: AsyncSession, id: int):
    db_item = await get_event_by_id(db, id)
    await db.delete(db_item)
    await db.commit()
    return {"message": "Item deleted successfully"}


async def update_event(db: AsyncSession, id : int, updates: Event):
    event = await get_event_by_id(db, id)
    if not event:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event, key, value)
    await db.commit()
    await db.refresh(event)
    return event

async def get_event_by_id(db: AsyncSession, id : int):
    result = await db.execute(
        select(EventBase).where(
            EventBase.id == id
        )
    )
    return result.scalar_one_or_none()

async def get_events(db: AsyncSession):
    result = await db.execute(
        select(EventBase)
    )
    return result.scalars().all()