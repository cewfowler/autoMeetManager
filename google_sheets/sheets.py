import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope);
client = gspread.authorize(creds);

def getDataFromSheet(sheet_url):
    # Open the sheet, get the records, and get the first row (has names, events)
    sheet = client.open_by_url(sheet_url).sheet1;
    data = sheet.get_all_records();
    row = sheet.row_values(1);

    #print("Row: ");
    #print(row);

    lowerRow = [item.lower() for item in row];
    events = { "50 fly":        2,
               "50 back":       3,
               "50 breast":     4,
               "50 free":       5,
               "100 fly":       6,
               "100 back":      7,
               "100 breast":    8,
               "100 free":      9,
               "100 im":        10,
               "200 fly":       11,
               "200 back":      12,
               "200 breast":    13,
               "200 free":      14,
               "200 im":        15,
               "400 im":        16,
               "500 free":      17,
               "1000 free":     17,
             };

    for event in events:
        # If event exists, add index to dictionary
        try:
            index = lowerRow.index(event);
            events[event] = index;
        # If event does not exist, set to -1
        except:
            events[event] = -1;

    # Remove events that don't exist
    events = {event:index for event, index in events.items() if index != -1};

    print("Events: ");
    print(events);

    for entry in data:
        print("Entry: ");
        print(entry);

        print("Timestamp: " + str( entry[row[0]] ));
        print("Name: " + str( entry[row[1]] ));
        break;


def main():
    getDataFromSheet("https://docs.google.com/spreadsheets/d/1r8Dn0gzlC2RoF6j2EH7q57u3r3VEdQPjz5651-OF1_g/edit#gid=882094980")

if __name__ == '__main__':
    main();
