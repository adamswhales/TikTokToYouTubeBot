import requests, os

def download_tiktok_video(video_url, output_folder="downloads"):
    lookup = requests.get(f"https://api.tikmate.app/api/lookup?url={video_url}")
    if lookup.status_code != 200:
        print("❌ Failed to fetch video info.")
        return None
    data = lookup.json()
    download_url = f"https://tikmate.app/download/{data['token']}/{data['id']}.mp4"
    filename = f"{output_folder}/{data['id']}.mp4"
    os.makedirs(output_folder, exist_ok=True)
    with open(filename, "wb") as f:
        f.write(requests.get(download_url).content)
    return filename
