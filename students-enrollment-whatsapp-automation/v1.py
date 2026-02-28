import pywhatkit
import datetime
import time

def send_message(number, message):
    try:
        pywhatkit.sendwhatmsg_instantly(
            number,
            message,
            # wait_time=15,
            # tab_close=True
        )
        print("Message sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    number = "+923454640859"
    message = "Professional WhatsApp Automation"
    for i in range(5):
        send_message(number, message)
  