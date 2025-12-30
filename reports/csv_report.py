import csv

def generate_csv(results):
    with open("summary_report.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "Summary"])
        for r in results:
            writer.writerow([r["file_name"], r["summary"]])
