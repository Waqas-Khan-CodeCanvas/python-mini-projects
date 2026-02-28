import pandas as pd
import pywhatkit
import time

# Load student data
data = pd.read_csv("students.csv")

# Example structure:
# phone,course
# +911111111111,python
# +922222222222,ai

group_links = {
    "python": "https://chat.whatsapp.com/xxxx",
    "ai": "https://chat.whatsapp.com/yyyy",
    "web": "https://chat.whatsapp.com/zzzz",
    "ml": "https://chat.whatsapp.com/aaaa",
    "data": "https://chat.whatsapp.com/bbbb"
}

for _, row in data.iterrows():
    message = f"""
Congratulations 🎉

You are selected for {row['course']} course.

Join your group here:
{group_links[row['course']]}
"""
    pywhatkit.sendwhatmsg_instantly(
        f"+{str(row['phone'])}",
        message,
        wait_time=20,
        tab_close=True
    )
    time.sleep(20)        