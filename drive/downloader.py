import io
from googleapiclient.http import MediaIoBaseDownload

SUPPORTED_TYPES = {
    'application/pdf': '.pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
    'text/plain': '.txt',
    'text/csv': '.csv',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': '.xlsx'
}

def list_files(service, folder_id):
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType)"
    ).execute()

    # filter only supported types
    files = [
        f for f in results.get('files', [])
        if f['mimeType'] in SUPPORTED_TYPES
    ]
    return files


def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()
