Excellent choice ✅
This is the correct professional approach.

We’ll set up WhatsApp Cloud API (official, free tier eligible for your 200 students).

Owned by Meta for WhatsApp.

🎯 WHAT YOU WILL ACHIEVE

After this setup, you will be able to:

Send 200 official WhatsApp messages

Include group invite link

Stay within free tier (1000 conversations/month)

Avoid ban risk

Build reusable system for future batches

🧱 STEP 1: Create Meta Developer App

Go to:

👉 Meta for Developers

Steps:

Login with Facebook account

Click My Apps

Click Create App

Choose:

Type: Business

Fill:

App Name

Email

Create

🧱 STEP 2: Add WhatsApp Product

Inside your App dashboard:

Click Add Product

Select WhatsApp

Click Set Up

You now get:

Temporary Access Token

Test Phone Number

Phone Number ID

WhatsApp Business Account ID

⚠️ Save:

Access Token

Phone Number ID

🧱 STEP 3: Send Test Message (Verify Working)

Install requests:

pip install requests
Python Test Script
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

Run it.

If successful → you’ll receive message instantly.

🧱 STEP 4: Add Your Own Business Phone Number

Now replace test number:

Go to WhatsApp → Getting Started

Click Add Phone Number

Verify via OTP

This number will send messages

⚠️ This number cannot already be active WhatsApp personal account.

🧱 STEP 5: Create Message Template (IMPORTANT)

Since students have not messaged you first, you MUST use template.

Go to:

WhatsApp Manager → Message Templates

Create template:

Example:

Template Name: course_selection_notice

Body:

Hello {{1}},

Congratulations 🎉
You have been selected for {{2}} course.

Please join your group:
{{3}}

Thank you.

Submit for approval (usually 5–30 minutes).

🧱 STEP 6: Send Template Message via Python

Now your professional script:

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
🧠 Free Tier Calculation

You send 200 students →
Each is 1 conversation →
Free limit = 1000/month

✅ You pay = 0

🛡 Professional Tips

Send slowly (1–2 sec delay)

Log failures

Validate phone format

Use country code (no + symbol)

Store token in environment variable

Don't hardcode secrets

⚠️ Important Rules

You cannot create WhatsApp groups via API

Students must click invite link themselves

Template approval required

Don't send promotional spam

🏗 If You Want Next Level

You can later add:

Webhook (to track replies)

Auto response system

Admin dashboard

Deployment on AWS

Database logging

🎯 Final Result

You will have:

Official system

Free

Ban-proof

Reusable every 6 months

Fully professional

If you want, next I can:

1️⃣ Draw complete architecture diagram
2️⃣ Help you with business verification
3️⃣ Help you deploy on VPS
4️⃣ Help you create production-ready project structure

Tell me what level you want next.