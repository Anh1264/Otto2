# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'credentials.json'
def get_drive_service():
    """Authenticate and return the Google Drive API service."""
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file_to_drive(file_data, file_name, folder_name):
    service = get_drive_service()
    folder_id = get_or_create_folder(service, folder_name)
    query = f"name='{file_name}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, spaces='drive', fields='files(id)').execute()
    items = results.get('files', [])

    if items:
        # File already exists, return the link to the existing file
        file_id = items[0]['id']
        return f"https://drive.google.com/uc?id={file_id}"
    file_metadata = {'name': file_name, 'parents': folder_id, }
    media = MediaFileUpload(file_data, mimetype='image/jpeg', resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    print('file_id:' ,file_id)
    permission =  {
        'type': 'anyone',
        'role': 'reader',
    }
    service.permissions().create(fileId=file_id, body=permission).execute()
    return f"https://drive.google.com/uc?id={file_id}"
    # return f"https://drive.google.com/thumbnail?id={file['id']}&sz=w1000"

def get_or_create_folder(service, folder_name):
    print('folder name: ', folder_name)
    """Get the folder ID by name, or create it if it doesn't exist."""
    # Search for the folder
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])

    if items:
        # Folder exists
        print('Folder id:', items[0]['id'])
        return items[0]['id']
    else:
        # Create new folder
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print('Folder id:', folder['id'])
        return folder['id']