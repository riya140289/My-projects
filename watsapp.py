import pywhatkit
from datetime import datetime, timedelta

# Phone number with country code
phone_number = "+91**********"

# Message
message = "Hello! This is a scheduled WhatsApp message."

# Schedule time (2 minutes from now)
now = datetime.now()
send_time = now + timedelta(minutes=2)

hour = send_time.hour
minute = send_time.minute

# Send message
pywhatkit.sendwhatmsg(
    phone_no=phone_number,
    message=message,
    time_hour=hour,
    time_min=minute,
    wait_time=15,
    tab_close=True,
    close_time=3
)

print(f"Message scheduled for {hour}:{minute}")
