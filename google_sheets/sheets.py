import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Get swimmer meet entries from google sheet
# Parameters:
#   sheetsRow: the first row of the google sheet with the field names (including
#        event names)
# Returns: the meet's events
def getMeetEvents(sheetsRow):
    lowerRow = [item.lower() for item in sheetsRow];
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

    # If event exists, add index to dictionary
    for e in events:
        try:
            index = lowerRow.index(e);
            events[e] = index;
        except:
            print(e + ' was not found for this meet.')
    print()

    # Remove events that don't exist in this meet
    events = {e:index for e,index in events.items() if index != -1};
    return events


# Get swimmer meet entries from google sheet
# Parameters:
#   events: array of events and their indices
#   times: the times the swimmer entered for their events
# Returns: the swimmer's meet entries
def getMeetEntries(events, times):
    entries = dict();
    for e in events:
        indexOfEvent = events[e];

        # Get events and corresponding times
        time = times[indexOfEvent];

        # If person entered time, add event to entries
        if (time):
            #print("Event: " + entry);
            #print("Time: " + time);
            entries.update({e: time})

    return entries;


# Get swimmer meet entries from google sheet
#   sheetUrl: default should not be used except for testing; contains the url
#       to the google sheet with the meet entries
# Returns: dict containing swimmers and all their entries
def getDataFromSheet(sheetUrl):
    # Authenticate for google sheets access
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credsFile = os.path.join(os.path.dirname(__file__), "creds.json");
    creds = ServiceAccountCredentials.from_json_keyfile_name(credsFile, scope);
    client = gspread.authorize(creds);

    # Open the sheet, get the records, and get the first row (has event names)
    sheet = client.open_by_url(sheetUrl).sheet1;
    allData = sheet.get_all_records();
    row = sheet.row_values(1);

    # Important indices
    nameIndex = row[1];
    idIndex = row[2];
    genderIndex = row[3];
    isNewSwimmerIndex = row[4];

    events = getMeetEvents(row);

    signups = dict();

    print("Signups: ");

    # Add each swimmer and their entries
    for item in allData:
        times = list(item.values());
        entries = getMeetEntries(events, times)
        id = item[idIndex];

        swimmerInfo = list();
        swimmerInfo["id"] = id;
        swimmerInfo["name"] = item[nameIndex];
        swimmerInfo["gender"] = item[genderIndex];
        swimmerInfo["isNewSwimmer"] = item[isNewSwimmerIndex];
        swimmerInfo["entries"] = entries;

        print(swimmerInfo["name"]);
        print(swimmerInfo["entries"]);
        print();

        signups.update({id: swimmerInfo});

    return signups;


def main():
    getDataFromSheet("https://docs.google.com/spreadsheets/d/1r8Dn0gzlC2RoF6j2EH7q57u3r3VEdQPjz5651-OF1_g/edit#gid=882094980")

if __name__ == '__main__':
    main();
