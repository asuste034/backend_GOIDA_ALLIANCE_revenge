from fastapi import FastAPI

app = FastAPI(title='Админка для UJIN')

from user.router import user_router
from auth.router import auth_router

app.include_router(auth_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)