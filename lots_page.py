from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import waitCheckHtmlExisting, convertToCsv

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

browser = webdriver.Chrome(options=options)
browser.get('https://www.copart.com/saleListResult/55/2023-12-14?location=FL%20-%20Orlando%20South&saleDate=1702566000000&liveAuction=false&from=&yardNum=55')


def parseTable():
  lots = []
  target  = (By.TAG_NAME, 'tbody')
  waitCheckHtmlExisting(browser, *target)

  table = browser.find_element(*target)
  rows = table.find_elements(By.TAG_NAME, 'tr')

  for row in rows:
    lot_title = row.find_element(By.CSS_SELECTOR, "span[class*='search_result_lot_detail ng-star-inserted']").text
    lot_id = row.find_element(By.CSS_SELECTOR, "span[class*='search_result_lot_number p-bold blue-heading ng-star-inserted']").text
    lot_link = row.find_element(By.TAG_NAME, 'a').get_attribute('href')
    price_div = row.find_element(By.CSS_SELECTOR, "div[class*='p-flex-column p-d-flex ng-star-inserted']")
    lot_bid = price_div.find_element(By.CLASS_NAME, 'currencyAmount').text
    lots.append([lot_id, lot_bid, lot_title, lot_link])

  convertToCsv(lots)

parseTable()
