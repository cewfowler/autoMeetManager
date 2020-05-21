import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope);
client = gspread.authorize(creds);

def getDataFromSheet(sheet_url):
    # Open the sheet, get the records, and get the first row (has names, events)
    sheet = client.open_by_url(sheet_url).sheet1;
    allData = sheet.get_all_records();
    row = sheet.row_values(1);

    #print("Row: ");
    #print(row);

    lowerRow = [item.lower() for item in row];
    events = { "50 fly":        -1,
               "50 back":       -1,
               "50 breast":     -1,
               "50 free":       -1,
               "100 fly":       -1,
               "100 back":      -1,
               "100 breast":    -1,
               "100 free":      -1,
               "100 im":        -1,
               "200 fly":       -1,
               "200 back":      -1,
               "200 breast":    -1,
               "200 free":      -1,
               "200 im":        -1,
               "400 im":        -1,
               "500 free":      -1,
               "1000 free":     -1,
             };

    for event in events:
        # If event exists, add index to dictionary
        try:
            index = lowerRow.index(event);
            events[event] = index;
        except:
            print(event + ' was not found for this meet.')
    print()

    # Remove events that don't exist in this meet
    events = {event:index for event, index in events.items() if index != -1};

    #print("Events: ");
    #print(events);
    signups = dict();

    print("Signups: ");
    for item in allData:
        #print("Timestamp: " + str( item[row[0]] ));
        #print("Name: " + str( item[row[1]] ));

        entries = dict();
        for event in events:

            # Get events and corresponding times
            entry = list(item.keys())[events[event]];
            time = list(item.values())[events[event]];

            # If person entered time, add event to entries
            if (time):
                #print("Event: " + entry);
                #print("Time: " + time);
                entries.update({entry: time})

        print(item[row[1]]);
        print(entries);
        print();

        # Add the person and their entries to signups
        signups.update({item[row[1]]: entries});


def main():
    getDataFromSheet("https://docs.google.com/spreadsheets/d/1r8Dn0gzlC2RoF6j2EH7q57u3r3VEdQPjz5651-OF1_g/edit#gid=882094980")

if __name__ == '__main__':
    main();
