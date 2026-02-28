# Send Test Message (Verify Working)


import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"

url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "messaging_product": "whatsapp",
    "to": "YOUR_PERSONAL_NUMBER_WITH_COUNTRY_CODE",
    "type": "text",
    "text": {
        "body": "Cloud API is working successfully ✅"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())