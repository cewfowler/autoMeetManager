import sys;
import pyautogui;
import argparse;
from config.configureApp import configureMeetManager, readConfigFile;
from google_sheets.sheets import getDataFromSheet;

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
def main(configure, sheetsUrl):
    if (configure):
        print('Beginning configuration...');
        configureMeetManager();

    config = readConfigFile();

    signups = getDataFromSheet(sheetsUrl);

    for swimmer in signups:
        print(swimmer["swimmerInfo"]["name"]);
        print(signups[swimmer])

    # pyautogui.moveTo(x, y, duration in seconds);


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Automate meet entries.");
    parser.add_argument('-c', '--config',
        action='store_true',
        help='When this flag is set, the program first configures the application.');
    parser.add_argument('-s','--sheet',
        help='The meet signup url for access to the google sheet.',
        default="https://docs.google.com/spreadsheets/d/1r8Dn0gzlC2RoF6j2EH7q57u3r3VEdQPjz5651-OF1_g/edit#gid=882094980");
    args = parser.parse_args();

    main(args.config, args.sheet);
