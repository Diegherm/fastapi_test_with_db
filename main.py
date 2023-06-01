from fastapi import FastAPI

from inventory.routes import router

app = FastAPI()

app.include_router(router, prefix="")
