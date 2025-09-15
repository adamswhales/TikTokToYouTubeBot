import schedule, time
from main import run_upload_batch

# Schedule 5 batches of 4 videos each
schedule.every().day.at("08:00").do(lambda: run_upload_batch(4))
schedule.every().day.at("11:00").do(lambda: run_upload_batch(4))
schedule.every().day.at("14:00").do(lambda: run_upload_batch(4))
schedule.every().day.at("17:00").do(lambda: run_upload_batch(4))
schedule.every().day.at("20:00").do(lambda: run_upload_batch(4))

print("📅 Scheduler running...")
while True:
    schedule.run_pending()
    time.sleep(60)
