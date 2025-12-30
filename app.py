from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pipeline import run_pipeline

FOLDER_ID = "1-TCeDyBi9jAte2WN0Gm3-9Il-_boD2bB"

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    results = run_pipeline(FOLDER_ID)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "results": results}
    )
