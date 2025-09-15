from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service():
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    return build("youtube", "v3", credentials=creds)

def upload_to_youtube(video_path, title):
    youtube = get_youtube_service()
    body = {
        "snippet": {
            "title": title,
            "description": "Reposted from TikTok",
            "tags": ["TikTok", "Shorts"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    }
    media = MediaFileUpload(video_path, mimetype="video/*", resumable=True)
    response = youtube.videos().insert(part="snippet,status", body=body, media_body=media).execute()
    print(f"✅ Uploaded: {response['id']}")
    return response['id']
