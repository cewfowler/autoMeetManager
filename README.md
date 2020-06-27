# Automated Meet Manager Entries #
#### Created by Chris F, 2020 ####

## Installation ##
### Mac OS ###
1. [Install python](https://programwithus.com/learn-to-code/install-python3-mac/)
2. Install the necessary packages:
```
pip3 install pyautogui readchar gspread oauth2client
```
- If there is an error using `pip3 install`, try `python3 -m pip install`.

## Setup ##
1. Create a new client key.
* Go to [Google Cloud Console](console.cloud.google.com) and click on the Navigation Bar. Select "APIs & Services->Credentials".
* Click on the MeetManager Service Account.
* On the bottom of the page, click *Create Key*.
* Make sure JSON is selected as the key type and a download should begin. Save the file as _**creds.json**_ and put it in the _**google_sheets**_ folder.
2. After creating the google form, open the response sheet. Click the *Share* button and go to _**creds.json**_ found in the _**google_sheets**_ directory. Copy the client_email (Ex. "meetmanager@future-sonar-276916.iam.gserviceaccount.com") and paste it in the share box. Then click *Done*.

## Running the program ##
1. Open the command line/terminal.
2. Run the program:
```
python3 <folder_location>/autoMeetManager/autoMeetManager.py --sheet <sheet_url>
```
  - _**\<folder\_location\>**_ is the location of the autoMeetManager
  application in your folder system. You can navigate to the
  _**autoMeetManager**_ folder so you can simply run:
  ```
  python3 autoMeetManager.py --sheet <sheet_url>
  ```
    - To navigate your file system from the command line use ```cd <subdirectory
    or path>``` to change directories, ```ls``` to check current subdirectories,
    and ```pwd``` to check the current directory.
  - _**\<sheet_url\>**_ is the url of the google sheet containing the meet entry
  data. To prevent errors, wrap the url in \"\".
  - To run with configuration setup (required on first run) add the _**-c**_ or
  _**--config**_ flag:
  ```
  python3 autoMeetManager.py --sheet <sheet_url> -c
  ```
3. Ensure the program is correctly configured by observing the first few
meet entries.


  [Getting Google Form Responses](https://www.youtube.com/watch?v=cnPlKLEGR7E)
