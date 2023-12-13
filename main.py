from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(options={})
browser.get('https://www.copart.com/todaysAuction')
browser.implicitly_wait(5)
links = browser.find_elements(By.LINK_TEXT, "View List")

for link in links:
  print(link.get_attribute("href"))
