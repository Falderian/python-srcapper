import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


def uploadCsv():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "client_secret.json", scope
    )
    client = gspread.authorize(credentials)

    spreadsheet = client.open("Auction-copart")

    def clearSheets():
        worksheets = spreadsheet.worksheets()
        reqs = [
            {"repeatCell": {"range": {"sheetId": s.id}, "fields": "*"}}
            if i == 0
            else {"deleteSheet": {"sheetId": s.id}}
            for i, s in enumerate(worksheets)
        ]
        spreadsheet.batch_update({"requests": reqs})

    clearSheets()
    sheetsPath = os.getcwd() + "/sheets/"
    for filename in os.listdir(sheetsPath):
        worksheet = spreadsheet.add_worksheet(title=filename, rows=100, cols=4)
        with open(sheetsPath + filename, "r") as file_obj:
            content = file_obj.read()
            body = {
                "requests": [
                    {
                        "pasteData": {
                            "data": content,
                            "delimiter": ",",
                            "coordinate": {"sheetId": worksheet.id},
                        }
                    }
                ]
            }
            spreadsheet.batch_update(body)


def getFileName(filePath: str) -> str:
    start_index = filePath.rindex("/") + 1
    return filePath[start_index : len(filePath)]


uploadCsv()
