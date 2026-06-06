from fastapi import FastAPI

app = FastAPI(title='Админка для UJIN')

from user.router import auth_router
app.include_router(auth_router)
from event.router import router as event_router
app.include_router(event_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)