from fastapi import FastAPI

app = FastAPI(title='Сервер')

from user.router import user_router
from auth.router import auth_router
from event.router import event_router

app.include_router(event_router)
app.include_router(user_router)
app.include_router(auth_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)