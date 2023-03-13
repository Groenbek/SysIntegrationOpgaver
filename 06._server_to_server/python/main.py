# poetry init
# poetry add fastapi uvicorn
# poetry shell
# touch app.py

from fastapi import FastAPI
from datetime import datetime

# code .

app = FastAPI()
@app.get("/date")
def get_date():
    return datetime.now()

# uvicorn main:app --reload


# Do the http request for date like it was done in app.js

# poetry add requests
# uvicorn main:app --reload

import requests

@app.get("/datefromexpress")
def get_date_from_express():
    response = requests.get("http://127.0.0.1:8080/date")
    date = response.json()
    return date

@app.get("/datengrok")
def _():
    response = requests.get("ngok url her")
    date = response.json()
    return date