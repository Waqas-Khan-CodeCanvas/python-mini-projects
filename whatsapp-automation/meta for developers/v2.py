# 🧱 STEP 6: Send Template Message via Python

# Now your professional script:



import requests
import pandas as pd
import time

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"

url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

group_links = {
    "python": "https://chat.whatsapp.com/xxxx",
    "ai": "https://chat.whatsapp.com/yyyy",
    "web": "https://chat.whatsapp.com/zzzz",
    "ml": "https://chat.whatsapp.com/aaaa",
    "data": "https://chat.whatsapp.com/bbbb"
}

data_csv = pd.read_csv("students.csv")

for _, row in data_csv.iterrows():
    payload = {
        "messaging_product": "whatsapp",
        "to": row['phone'],
        "type": "template",
        "template": {
            "name": "course_selection_notice",
            "language": {"code": "en"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": row['name']},
                        {"type": "text", "text": row['course']},
                        {"type": "text", "text": group_links[row['course']]}
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    time.sleep(2)  # rate limit safety