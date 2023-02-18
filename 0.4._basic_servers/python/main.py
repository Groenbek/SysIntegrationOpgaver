# Poetry init, poetry shell, poetry add fastapi uvicorn,
# For at køre serveren skriv i terminalen skriv uvicorn main:app --reload

from fastapi import FastAPI
import json

app = FastAPI()

data_files = ["me.csv", "me.json", "me.txt", "me.xml", "me.yaml"]



@app.get("/")
def root():
    return {"message": "Sup FastAPI nerds"}

@app.get("/newroute")
def _():
    return {"message": "This is a new route"}

# Route to return data from me.json file
@app.get("/mejson")
def get_me_json():
    with open("me_files/me.json", "r") as f:
        data = json.load(f)
    return data

# Route to return data from me.csv file
@app.get("/mecsv")
def get_me_csv():
    with open("me_files/me.csv", "r") as f:
        data = f.read()
    return data

# Route to return data from me.txt file
@app.get("/metxt")
def get_me_txt():
    with open("me_files/me.txt", "r") as f:
        data = f.read()
    return data

# Route to return data from me.xml file
@app.get("/mexml")
def get_me_xml():
    with open("me_files/me.xml", "r") as f:
        data = f.read()
    return data

# Route to return data from me.yaml file
@app.get("/meyaml")
def get_me_yaml():
    with open("me_files/me.yaml", "r") as f:
        data = f.read()
    return data