from random import choice

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import json

app = FastAPI()

with open("theories/theories.json") as f:
    theories = json.load(f)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    theory = choice(theories)
    return templates.TemplateResponse("theory.html", {"request": request, "theory": theory})

@app.get("/_list", response_class=HTMLResponse)
def list_theories(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "theories": theories})
