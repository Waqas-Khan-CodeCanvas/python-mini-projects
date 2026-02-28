from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import time
import os


class WhatsAppBot:
    def __init__(self, driver_path, profile_path=None):

        options = Options()

        # Stability flags (important for Windows)
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")

        # Persistent login profile (absolute path)
        if profile_path:
            abs_profile = os.path.abspath(profile_path)
            options.add_argument(f"user-data-dir={abs_profile}")

        # Use manually downloaded chromedriver
        service = Service(driver_path)

        self.driver = webdriver.Chrome(
            service=service,
            options=options
        )

        self.wait = WebDriverWait(self.driver, 40)

        # Open WhatsApp Web
        self.driver.get("https://web.whatsapp.com")

        print("Scan QR Code if not logged in...")

        # Wait until chats load
        self.wait.until(
            EC.presence_of_element_located((By.ID, "pane-side"))
        )

        print("WhatsApp Web Ready!")

    def send_message(self, phone_number, message):

        encoded_message = quote(message)

        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        self.driver.get(url)

        try:
            message_box = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
                )
            )

            time.sleep(2)
            message_box.send_keys(Keys.ENTER)

            print(f"Message sent to {phone_number}")

        except Exception as e:
            print("Error sending message:", e)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":

    DRIVER_PATH = r"chromedriver.exe"
    PROFILE_PATH = "chrome_profile"   # auto-created folder

    bot = WhatsAppBot(
        driver_path=DRIVER_PATH,
        profile_path=PROFILE_PATH
    )

    number = "923454640859"  # without +
    message = "Professional WhatsApp Automation with Selenium"

    for i in range(2):
        bot.send_message(number, message)
        time.sleep(8)  # delay to reduce spam risk

    bot.close()