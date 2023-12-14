from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

browser = webdriver.Chrome(options=options)
browser.get('https://www.copart.com/todaysAuction')

WebDriverWait(browser,100).until(EC.presence_of_element_located((By.LINK_TEXT, "View List")))

links = browser.find_elements(By.LINK_TEXT, "View List")
print(f'There is {len(links)} links to scrap')

for link in links:
  print(link.get_attribute("href"))
