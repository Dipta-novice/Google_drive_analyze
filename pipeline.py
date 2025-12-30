from drive.auth import get_drive_service
from drive.downloader import list_files, download_file
from parser.extractor import extract_text
from summarizer.chain import summarize_text
from reports.csv_report import generate_csv

def run_pipeline(folder_id):
    service = get_drive_service()
    files = list_files(service, folder_id)

    results = []

    for file in files:
        file_name = file["name"]

        download_file(service, file["id"], file_name)
        text = extract_text(file_name)

        if not text.strip():
            continue

        summary = summarize_text(text)

        results.append({
            "file_name": file_name,
            "summary": summary
        })

    generate_csv(results)
    return results
