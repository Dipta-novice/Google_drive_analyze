from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_drive_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\Users\Puspita Sinha\Desktop\Google_drive_analyze\client_secret.json', SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)
