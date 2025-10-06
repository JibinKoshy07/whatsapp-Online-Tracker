from selenium import webdriver
import time
from colorama import Fore, Style, init

# Initialize colorama (for Windows/Linux compatibility)
init(autoreset=True)

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

input("Scan QR and press Enter...")

while True:
    try:
        status = driver.find_element("xpath", "//span[@title='online']")
        print(Fore.GREEN + Style.BRIGHT + "User is online!" + Style.RESET_ALL)
    except:
        print("User is offline.")
    time.sleep(10)
