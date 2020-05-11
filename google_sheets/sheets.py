import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope);
client = gspread.authorize(creds);

#def getDataFromSheet(sheet_name) {

#}

sheet = client.open("FSU Fear The Spear Meet Signup  (Responses)").sheet1;

data = sheet.get_all_records();

row = sheet.row_values(1);
print(row);

for entry in data:
    print("Timestamp: " + str( entry[row[0]] ));
    print("Name: " + str( entry[row[1]] ));
    break;
