# scripts/send_whatsapp.py
import pandas as pd
import pywhatkit as kit
import time

# Read Excel with links
df = pd.read_excel("../output/students_with_links.xlsx")

# Optional: Delay between messages to avoid WhatsApp rate limits
DELAY_SECONDS = 15

for index, row in df.iterrows():
    phone = row["Phone"]
    message = f"Hello {row['Name']}, welcome to {row['Course']} group!\nJoin here: {row['WhatsApp_Link']}"
    
    try:
        print(f"📩 Sending message to {row['Name']} ({phone})")
        # Send instantly, close tab automatically
        kit.sendwhatmsg_instantly(phone_no=phone, message=message, wait_time=15, tab_close=True)
        time.sleep(DELAY_SECONDS)  # Wait to avoid flooding
    except Exception as e:
        print(f"❌ Failed to send message to {row['Name']}: {e}")

print("✅ All WhatsApp messages sent!")
