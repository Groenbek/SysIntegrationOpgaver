from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
from datetime import datetime
import asyncio

print(datetime.now)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sse")
async def sse(request: Request):

    
