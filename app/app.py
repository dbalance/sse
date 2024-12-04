from fastapi import FastAPI
from .proxy import r


app = FastAPI()


app.include_router(r, prefix='/sse', tags=['sse'])