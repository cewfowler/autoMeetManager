# Automated Meet Manager Entries #

## Installation ##
### Mac OS ###
1. [Install python](https://programwithus.com/learn-to-code/install-python3-mac/)
2. Install the necessary packages:
```
pip3 install pyautogui
pip3 install readchar
pip3 install gspread
pip3 install oauth2client
```
- If there is an error using `pip3 install`, try `python3 -m pip install`.

## Setup ##
1. Create a new client key.
* Go to [Google Cloud Console](console.cloud.google.com) and click on the Navigation Bar. Select "APIs & Services->Credentials".
* Click on the MeetManager Service Account.
* On the bottom of the page, click *Create Key*.
* Make sure JSON is selected as the key type and a download should begin. Save the file as "creds.json" and put it in the "google_sheets" folder.
2. After creating the google form, open the response sheet. Click the *Share* button and go to "creds.json" found in the "google_sheets" directory. Copy the client_email (Ex. "meetmanager@future-sonar-276916.iam.gserviceaccount.com") and paste it in the share box. Then click *Done*.
3. In sheets.py change the url in the open_by_url function call to the url of the meet entries sheet.

## Running the program ##
1. Open the command line/terminal.
2. Run `python3 folder_location/autoMeetManager/autoMeetManager.py` using the
correct path.
  - _**folder\_location**_ is the location of the autoMeetManager application in your folder system.
  - To navigate your file system from the command line use ```cd <subdirectory or path>``` to change directories, ```ls``` to check current subdirectories, and ```pwd``` to check the current directory.


  [Getting Google Form Responses](https://www.youtube.com/watch?v=cnPlKLEGR7E)
