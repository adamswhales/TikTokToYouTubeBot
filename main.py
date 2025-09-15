import json, os, re, requests
from datetime import datetime
from tiktok_downloader import download_tiktok_video
from youtube_uploader import upload_to_youtube

# CONFIG
TIKTOK_USERNAME = "example_user"  # ← Replace with your actual TikTok username
LOG_FILE = "uploaded.json"
DOWNLOAD_FOLDER = "downloads"

# Ensure downloads folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Scrape TikTok video URLs
def get_tiktok_video_urls(username):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.tiktok.com/@{username}"
    try:
        html = requests.get(url, headers=headers).text
        return list(set(re.findall(r'https://www\.tiktok\.com/@[^"]+/video/\d+', html)))
    except Exception as e:
        print(f"❌ Failed to fetch TikTok page: {e}")
        return []

# Load uploaded log
def load_uploaded():
    if os.path.exists(LOG_FILE):
        try:
            return json.load(open(LOG_FILE))
        except:
            return []
    return []

# Save uploaded log
def save_uploaded(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f)

# Upload batch of videos
def run_upload_batch(batch_size):
    print(f"🚀 Starting batch at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    uploaded = load_uploaded()
    urls = get_tiktok_video_urls(TIKTOK_USERNAME)
    new_urls = [url for url in urls if url not in uploaded][:batch_size]

    if not new_urls:
        print("📭 No new videos to upload.")
        return

    for url in new_urls:
        try:
            video_path = download_tiktok_video(url, DOWNLOAD_FOLDER)
            if video_path:
                title = f"TikTok Repost {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                upload_to_youtube(video_path, title)
                uploaded.append(url)
                save_uploaded(uploaded)
                os.remove(video_path)  # 🧹 Clean up after upload
                print(f"🗑️ Deleted local file: {video_path}")
        except Exception as e:
            print(f"❌ Error processing {url}: {e}")
