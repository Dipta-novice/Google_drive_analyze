from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import csv
import io

from pipeline import run_pipeline

FOLDER_ID = "1LxALMQ2yyCDuzeSD9k_Zsxr3V_BRQP8E"

app = FastAPI(title="Drive Analyzer")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    results = run_pipeline(FOLDER_ID)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "results": results}
    )


@app.get("/download/csv")
def download_csv():
    results = run_pipeline(FOLDER_ID)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["File Name", "Summary", "File Link"])

    for item in results:
        writer.writerow([
            item["file_name"],
            item["summary"],
            item.get("file_link", "")
        ])

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=summaries.csv"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
