# 📄 Google Drive Document Analyzer & Summarizer

A FastAPI-based application that integrates with **Google Drive**, parses documents, generates **AI-powered summaries**, and presents the output via a **web interface** and **downloadable reports**.

---

## 🚀 Features

* ✅ **Google Drive Integration**

  * Reads documents from a specified Google Drive folder
* ✅ **Document Parsing**

  * Supports parsing text from PDF and Google Docs files
* ✅ **AI Summarization**

  * Uses an LLM to generate concise summaries of documents
* ✅ **Output Rendering**

  * Displays summaries in a styled web UI
  * Allows downloading summaries as a CSV report

---

## 🛠️ Tech Stack

* **Backend**: Python, FastAPI
* **Frontend**: HTML, Jinja2 Templates
* **AI/LLM**: Gemini / OpenAI (configurable)
* **Google APIs**: Google Drive API
* **Document Parsing**: PyPDF / Google Docs export
* **Server**: Uvicorn

---

## 📁 Project Structure

```
project/
│── app.py                 # FastAPI entry point
│── pipeline.py            # Drive → Parse → Summarize pipeline
│── requirements.txt
│── README.md
│
├── templates/
│   └── index.html         # HTML UI for displaying summaries
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/drive-document-analyzer.git
cd drive-document-analyzer
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Google Drive API Setup

1. Go to **Google Cloud Console**
2. Create a project
3. Enable **Google Drive API**
4. Create **OAuth 2.0 credentials**
5. Download `credentials.json`
6. Place it in the project root

> ⚠️ Ensure your Google account is added as a **test user** if the app is not verified.

---

### 5️⃣ Configure Folder ID

Update the Drive folder ID in `app.py`:

```python
FOLDER_ID = "YOUR_GOOGLE_DRIVE_FOLDER_ID"
```

---

### 6️⃣ Run the Application

```bash
uvicorn app:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 🖥️ Output

### Web Output

* Displays document summaries in a **styled HTML table**
* Provides **clickable links** to original Google Drive files

### Downloadable Output

* CSV report containing:

  * File name
  * Summary
  * File link

Endpoint:

```
/download/csv
```

---

## 🔍 Pipeline Overview

```text
Google Drive Folder
        ↓
Download / Export Documents
        ↓
Parse Document Text
        ↓
AI-based Summarization
        ↓
Web UI + CSV Report
```

---

## 📌 Notes

* The application currently supports **read-only Drive access**
* Large documents are chunked before summarization
* OAuth tokens are stored locally during development


## 👤 Author

**Dipta Chatterjee**
Data Scientist | GenAI & LLM Applications




