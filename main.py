from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auction_parser import parseAuction
from datetime import datetime
from helpers import removeAllFiles

start_time = datetime.now()

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)
browser.get("https://www.copart.com/todaysAuction")

removeAllFiles()

WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.LINK_TEXT, "View List"))
)

links = browser.find_elements(By.LINK_TEXT, "View List")
print(f"There is {len(links)} auctions to scrap")

for i in range(0, len(links)):
    print(links[i].get_attribute("href"))
    parseAuction(links[i].get_attribute("href"))

end_time = datetime.now()
print("Completed in: ", end_time - start_time)
