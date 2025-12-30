from parser.pdf_parser import parse_pdf
from parser.docx_parser import parse_docx
from parser.txt_parser import parse_txt
from parser.csv_parser import parse_csv
from parser.xlsx_parser import parse_xlsx

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)

    elif file_path.endswith(".docx"):
        return parse_docx(file_path)

    elif file_path.endswith(".txt"):
        return parse_txt(file_path)

    elif file_path.endswith(".csv"):
        return parse_csv(file_path)

    elif file_path.endswith(".xlsx"):
        return parse_xlsx(file_path)

    else:
        return ""
