import sys;
import pyautogui;
import argparse;
from config.configureApp import configureMeetManager, readConfigFile;
from google_sheets.sheets import getDataFromSheet;
from functionality.addAthlete import addAthlete;

# Get OS
os = sys.platform;
print("Operating system:", os);

# Get screen width + height
width, height = pyautogui.size();
print("Screen size:", width, ",", height, "pixels");

# Acceptable OS's are 'linux' (Linux), 'win32' (Windows), 'darwin' (macOS)
if (os.startswith('darwin')):
    print("Running on MacOS system");
elif (os.startswith('win32')):
    print("Running on Windows32 system");
elif (os.startswith('linux')):
    print("Running on Linux system");
else:
    print("System not recognized. Please try again on a Linux, Windows32, or MacOS system.");

###### Main application ######
#   configure: default=False; this flag determines whether the program will
#       first configure the necessary mouse locations
#   sheetsUrl: default should not be used except for testing; contains the url
#       to the google sheet with the meet entries
#   dur: the duration of the pyautogui commands
def main(configure, sheetsUrl, dur):
    if (configure):
        print('Beginning configuration...');
        configureMeetManager();

    config = readConfigFile();

    if (config == []):
        print("App has not been configured yet. Let's set up the configuration.");
        configureMeetManager();

    addAthleteBtnPos = config["addAthleteBtnPos"];
    team = config["team"];

    signups = getDataFromSheet(sheetsUrl);

    for swimmer in signups:
        # Add new swimmers
        if (swimmer["isNewSwimmer"]):
            addAthlete(addAthleteBtnPos, swimmer, team, dur);


        print(swimmer["name"]);
        print(swimmer["entries"]);

    # pyautogui.moveTo(x, y, duration in seconds);


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Automate meet entries.");
    parser.add_argument('-c', '--config',
        action='store_true',
        help='When this flag is set, the program first configures the application.');
    parser.add_argument('-s','--sheet',
        help='The meet signup url for access to the google sheet.',
        default="https://docs.google.com/spreadsheets/d/1r8Dn0gzlC2RoF6j2EH7q57u3r3VEdQPjz5651-OF1_g/edit#gid=882094980");
    parser.add_argument('--very_slow',
        action='store_true',
        help='Sets the duration of the pyautogui commands to 4 seconds.');
    parser.add_argument('--slow',
        action='store_true',
        help='Sets the duration of the pyautogui commands to 1 second.');
    parser.add_argument('--med',
        action='store_true',
        help='Sets the duration of the pyautogui commands to 0.5 seconds.');
    parser.add_argument('--fast',
        action='store_true',
        help='Sets the duration of the pyautogui commands to 0.1 seconds.');
    parser.add_argument('-d','--dur',
        action='store',
        help='Sets the duration of the pyautogui commands to the input.');

    args = parser.parse_args();
    dur = 0.1;
    if (args.very_slow):
        dur = 4;
    else if (args.slow):
        dur = 1;
    else if (args.med):
        dur = 0.5;
    else if (args.fast):
        dur = 0.1;
    else if (args.dur):
        dur = args.dur;

    main(args.config, args.sheet, dur);
