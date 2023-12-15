import csv
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waitCheckHtmlExisting(browser, selector, text):
    return WebDriverWait(browser, 200).until(
        EC.presence_of_element_located((selector, text))
    )


def waitUntilHtmlElClickable(browser, element):
    return WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element))


def convertToCsv(filename: str, lots: list[str]):
    column_names = ["lot", "last bid", "title", "url"]
    path_to_file = os.getcwd() + "/sheets/" + filename
    write_mode = "a" if os.path.exists(path_to_file) else "w"

    with open(path_to_file, write_mode, newline="") as file:
        write = csv.writer(file)

        if write_mode.__eq__("w"):
            write.writerow(column_names)
        write.writerows(lots)


def getAuctionName(auctionUrl: str) -> str:
    aucNameStartIndex = auctionUrl.index("=") + 1
    aucNameEndIndex = auctionUrl.index("&saleDate")
    aucitonName = auctionUrl[aucNameStartIndex:aucNameEndIndex].replace("%20", "")
    return aucitonName


def removeAllFiles():
    for file in os.scandir(os.getcwd() + "/sheets/"):
        os.unlink(file.path)
