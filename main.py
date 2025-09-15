import json, os, re, requests
from datetime import datetime
from tiktok_downloader import download_tiktok_video
from youtube_uploader import upload_to_youtube

TIKTOK_USERNAME = "example_user"
LOG_FILE = "uploaded.json"
DOWNLOAD_FOLDER = "downloads"

def get_tiktok_video_urls(username):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.tiktok.com/@{username}"
    html = requests.get(url, headers=headers).text
    return list(set(re.findall(r'https://www\.tiktok\.com/@[^"]+/video/\d+', html)))

def load_uploaded():
    if os.path.exists(LOG_FILE):
        return json.load(open(LOG_FILE))
    return []

def save_uploaded(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f)

def run_upload_batch(batch_size):
    print(f"🚀 Starting batch at {datetime.now()}")
    uploaded = load_uploaded()
    urls = get_tiktok_video_urls(TIKTOK_USERNAME)
    new_urls = [url for url in urls if url not in uploaded][:batch_size]

    for url in new_urls:
        try:
            video_path = download_tiktok_video(url, DOWNLOAD_FOLDER)
            if video_path:
                title = f"TikTok Repost {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                upload_to_youtube(video_path, title)
                uploaded.append(url)
                save_uploaded(uploaded)
        except Exception as e:
            print(f"❌ Error: {e}")
