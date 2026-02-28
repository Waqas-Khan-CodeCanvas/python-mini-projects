# scripts/generate_links.py
import pandas as pd
from config import course_links

# Step 1: Read student data
df = pd.read_excel("../data/students.xlsx")

# Step 2: Generate personalized WhatsApp links
def create_whatsapp_link(name, course):
    base_link = course_links.get(course, "")
    # Encode spaces in URL
    text_message = f"Hello {name}, welcome to {course} group!".replace(" ", "%20")
    return f"{base_link}?text={text_message}"

df["WhatsApp_Link"] = df.apply(lambda row: create_whatsapp_link(row["Name"], row["Course"]), axis=1)

# Step 3: Save updated Excel
df.to_excel("../output/students_with_links.xlsx", index=False)
print("✅ Personalized WhatsApp links generated successfully!")
