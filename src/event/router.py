from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from event import services
from event.schemes import EventResponse, Event

event_router = APIRouter(prefix="/events", tags=["events"])

@event_router.post('/create', response_model=EventResponse)
async def create_event(event: Event, db: AsyncSession = Depends(get_db)):
    return await services.create_event(db, event)

@event_router.get('/get', response_model=list[EventResponse])
async def get_events(db: AsyncSession = Depends(get_db)):
    return services.get_events(db)

@event_router.put('/update/{event_id}', response_model=EventResponse)
async def update_event(event_id: int, updates: Event, db : AsyncSession = Depends(get_db)):
    event = await services.update_event(db, event_id, updates)
    if not event:
        raise HTTPException(status_code=404, detail="ШАБЛОН НЕ НАЙДЕН")
    return event

@event_router.delete('/delete/{event_id}')
async def delete_event(event_id: int, db : AsyncSession = Depends(get_db)):
    event = await services.delete_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="ШАБЛОН НЕ НАЙДЕН")
    return {"message" : "Шаблон удален успешно"}

@event_router.get('/events/{event_id}', response_model=EventResponse)
async def get_event(event_id: int, db: AsyncSession = Depends(get_db)):
    return await services.get_event_by_id(db, event_id)