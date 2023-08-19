from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from models import *

app=FastAPI()

@app.get("/")
def index():
    return {"message ":"hello"}


register_tortoise(
    app,
    db_url ="asyncpg://gurumanglam:Guru@035@localhost:5432/e_commerce_db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)



