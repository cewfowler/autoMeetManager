import sys;
import pyautogui;
import json;
import readchar;

# Reads config info
def readConfigFile():
    try:
        with open('config/config.json', 'r') as f:
            config = json.load(f);
            f.close();

        return config;
    except:
        return {};

# Writes updated config info
def updateConfigFile(updatedConfig):
    with open('config/config.json', 'w+') as f:
        json.dump(updatedConfig, f);
        f.close();

def adjustCursor(x, y):
    width, height = pyautogui.size();
    wrongKeyAttempts = 3;
    print('x-axis: ' + str(x) + '% from the left');
    print('y-axis: ' + str(y) + '% from the bottom');

    print('Adjust the cursor using your arrow keys (do not hold down or press too fast). Press \'c\' to cancel.\n');
    while(True):
        # Update cursor and get user key press
        pyautogui.moveTo(width * x/100, height * (100 - y)/100, duration=0.1);
        key = readchar.readkey();

        # Map keyboard press to cursor movement, cancel, or continue
        if (key == readchar.key.UP):
            wrongKeyAttempts = 3;

            if (y < 100):
                y = y + 1;
            else:
                print("Can not move any further up!");

        elif (key == readchar.key.DOWN):
            wrongKeyAttempts = 3;

            if (y > 0):
                y = y - 1;
            else:
                print("Can not move any further down!");

        elif (key == readchar.key.LEFT):
            wrongKeyAttempts = 3;

            if (x > 0):
                x = x - 1;
            else:
                print("Can not move any further left!");

        elif (key == readchar.key.RIGHT):
            wrongKeyAttempts = 3;

            if (x < 100):
                x = x + 1;
            else:
                print("Can not move any further right!");

        elif (key == readchar.key.ENTER):
            print("New x-axis val: " + str(x) + "% from the left");
            print('New y-axis val: ' + str(y) + '% from the bottom');
            break;

        elif (key == 'c'):
            print("Configuration cancelled.");
            return -1, -1;

        else:
            print("Invalid key pressed! Please enter a valid key. ")
            wrongKeyAttempts = wrongKeyAttempts - 1;
            print("Wrong key attempts left: " + str(wrongKeyAttempts));

            if (wrongKeyAttempts <= 0):
                print("Clearly this is too complicated for you to handle...");
                break;

    return x, y;

def configureMeetManager():
    config = readConfigFile();
    try:
        startAppPos = config["startAppPos"];
    except:
        startAppPos = {"x": 10, "y": 10}

    try:
        events = config["events"];
    except:
        events = { "50 fly":        {"x": 10, "y": 10},
                   "50 back":       {"x": 10, "y": 10},
                   "50 breast":     {"x": 10, "y": 10},
                   "50 free":       {"x": 10, "y": 10},
                   "100 fly":       {"x": 10, "y": 10},
                   "100 back":      {"x": 10, "y": 10},
                   "100 breast":    {"x": 10, "y": 10},
                   "100 free":      {"x": 10, "y": 10},
                   "100 im":        {"x": 10, "y": 10},
                   "200 fly":       {"x": 10, "y": 10},
                   "200 back":      {"x": 10, "y": 10},
                   "200 breast":    {"x": 10, "y": 10},
                   "200 free":      {"x": 10, "y": 10},
                   "200 im":        {"x": 10, "y": 10},
                   "400 im":        {"x": 10, "y": 10},
                   "500 free":      {"x": 10, "y": 10},
                   "1000 free":     {"x": 10, "y": 10},
                 };

    x = startAppPos["x"];
    y = startAppPos["y"];

    print("Setup for application start:\n")
    newX,newY = adjustCursor(x,y);
    if (newX == -1 and newY == -1):
        print("Update config cancelled.")
        return -1;

    startAppPos["x"] = newX;
    startAppPos["y"] = newY;
    updateConfigFile({"startAppPos": startAppPos});
    print("Updated config file!");

    return 0;
