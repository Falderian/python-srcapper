from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import os

def waitCheckHtmlExisting(browser, selector, text):
  return WebDriverWait(browser,200).until(EC.presence_of_element_located((selector, text)))

def waitUntilHtmlElClickable(browser, element):
  return WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element))

def convertToCsv(filename: str, lots: list[str]):
  column_names = ['lot','last bid', 'title', 'url']
  path_to_sheets_dir = os.getcwd() + '\\sheets\\' + filename

  with open(path_to_sheets_dir, 'w', newline='') as file:
    write = csv.writer(file)

    write.writerow(column_names)
    write.writerows(lots)
