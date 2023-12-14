from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv

def waitCheckHtmlExisting(browser, selector, text):
  return WebDriverWait(browser,100).until(EC.presence_of_element_located((selector, text)))

def convertToCsv(lots: list[str]):
  column_names = ['lot','last bid', 'title', 'url']

  with open('lots.csv', 'w', newline='') as file:
    write = csv.writer(file)

    write.writerow(column_names)
    write.writerows(lots)
