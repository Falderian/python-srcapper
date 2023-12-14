import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

def uploadCsv():
  credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
  client = gspread.authorize(credentials)

  spreadsheet = client.open('Auction-copart')

  with open('/sheets/lots.csv', 'r') as file_obj:
      content = file_obj.read()
      client.import_csv(spreadsheet.id, data=content)
