from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import (
    waitCheckHtmlExisting,
    convertToCsv,
    waitUntilHtmlElClickable,
    getAuctionName,
)
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)

tableTarget = (By.TAG_NAME, "tbody")


def parseAuction(url: str):
    browser.get(url)
    waitCheckHtmlExisting(browser, *tableTarget)

    pagiantionTarget = (
        By.CSS_SELECTOR,
        "div[class*='p-paginator-rpp-options p-dropdown p-component']",
    )
    waitCheckHtmlExisting(browser, *pagiantionTarget)

    pagination = browser.find_element(*pagiantionTarget)
    dropdownTrigger = pagination.find_element(
        By.CSS_SELECTOR,
        "span[class*='p-element p-dropdown-label p-inputtext ng-star-inserted']",
    )

    sleep(1)
    dropdownTrigger.click()
    sleep(1)

    dropdownWrapper = browser.find_element(By.CLASS_NAME, "p-dropdown-items-wrapper")
    selectOption100 = dropdownWrapper.find_elements(
        By.CSS_SELECTOR, "li[class*='p-ripple p-element p-dropdown-item']"
    )[4]

    waitUntilHtmlElClickable(browser, selectOption100)
    selectOption100.click()
    sleep(1)
    parseTable(url)


def parseTable(auctionUrl: str):
    lots = []

    waitCheckHtmlExisting(browser, *tableTarget)
    pageButtons = browser.find_elements(
        By.CSS_SELECTOR,
        "button[class*='p-ripple p-element p-paginator-page p-paginator-element p-link ng-star-inserted']",
    )

    getLots(lots)

    for button in pageButtons:
        button.click()
        sleep(3)
        getLots(lots)

    filename = getAuctionName(auctionUrl)
    convertToCsv(filename, lots)


def getLots(lots: list):
    table = browser.find_element(*tableTarget)
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        lot_title = row.find_element(
            By.CSS_SELECTOR, "span[class*='search_result_lot_detail ng-star-inserted']"
        ).text
        lot_id = row.find_element(
            By.CSS_SELECTOR,
            "span[class*='search_result_lot_number p-bold blue-heading ng-star-inserted']",
        ).text
        lot_link = row.find_element(By.TAG_NAME, "a").get_attribute("href")
        price_div = row.find_element(
            By.CSS_SELECTOR, "div[class*='p-flex-column p-d-flex ng-star-inserted']"
        )
        lot_bid = price_div.find_element(By.CLASS_NAME, "currencyAmount").text
        lots.append([lot_id, lot_bid, lot_title, lot_link])
