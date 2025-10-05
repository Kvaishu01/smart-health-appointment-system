import schedule
import time

# Sample patient data
patients = [
    {"name": "John Doe", "appointment_time": "10:00 AM"},
    {"name": "Alice Smith", "appointment_time": "2:30 PM"},
]

# Function to send notifications (Console Output Only)
def send_notifications():
    print("\n🚀 Sending notifications...")
    
    for patient in patients:
        message = f"📢 Reminder: {patient['name']}, your appointment is at {patient['appointment_time']}."
        print(message)

    print("✅ Notification process completed.\n")

# Schedule reminders (Runs every day at 9:13 AM)
schedule.every().day.at("09:13").do(send_notifications)

print("✅ Notification system started. Waiting for scheduled time...")

# 🚀 Run notifications immediately for testing
send_notifications()

# Keep the script running
while True:
    schedule.run_pending()
    print("🔄 Checking schedule...")
    time.sleep(60)  # Check every minute


'''

Your script is working perfectly! 🎉

What Happened?
Notification system started. ✅
Sent notifications immediately (for testing). 🚀
Printed reminders for both patients. 📢
Now waiting for the scheduled time (09:13 AM) to run again. 🔄
Next Steps
🔹 If you want to change the scheduled time, update this line:
schedule.every().day.at("09:13").do(send_notifications)
For example, to run at 10:00 AM, change it to:

schedule.every().day.at("10:00").do(send_notifications)
🔹 If you want notifications every few minutes (for testing), replace the scheduling with:

schedule.every(1).minutes.do(send_notifications)  # Runs every 1 minute
This will trigger notifications every minute instead of waiting for the next day.

🚀 Your script is running correctly! Let me know if you need further modifications. 🔥



'''