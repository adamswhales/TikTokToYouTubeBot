# TikTok to YouTube Shorts Automation

Automatically reposts TikTok videos from a public account to YouTube Shorts—up to 20 per day.

## Features
- ✅ Watermark-free TikTok downloads via TikMate API
- ✅ YouTube Shorts uploads with OAuth
- ✅ Daily scheduling in batches
- ✅ Duplicate protection via `uploaded.json`

## Setup
1. Clone this repo to Replit or your server
2. Upload `client_secrets.json` and `token.json` from Google Cloud Console
3. Create a blank `uploaded.json` file
4. Run `scheduler.py` to start automation

## Notes
- Make sure the TikTok account is public
- YouTube videos must be vertical and under 60 seconds
- You can customize the schedule in `scheduler.py`
