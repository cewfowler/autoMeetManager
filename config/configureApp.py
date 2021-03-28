import sys;
import pyautogui;
import json;
import readchar;
from adjustCursor import configureCursor

# Reads config info
# Returns: config object or empty object if there is an error
def readConfigFile():
    try:
        with open('config/config.json', 'r') as f:
            config = json.load(f);
            f.close();

        return config;
    except:
        return {};

# Writes updated config info
#   updatedConfig: value to update
def updateConfigFile(updatedConfig):
    with open('config/config.json', 'w+') as f:
        json.dump(updatedConfig, f);
        f.close();

# Configure all the mouse locations for the application
# Returns: 0 if config was successful, -1 otherwise
def configureMeetManager():
    config = readConfigFile();

    try:
        startAppBtnPos = config["startAppBtnPos"];
    except:
        startAppBtnPos = {"x": 10, "y": 10};

    try:
        athletesBtnPos = config["athletesBtnPos"];
    except:
        athletesBtnPos = {"x": 10, "y": 10};

    try:
        addAthleteBtnPos = config["addAthleteBtnPos"];
    except:
        addAthleteBtnPos = {"x": 10, "y": 10};

    try:
        addAthleteOkBtnPos = config["addAthleteOkBtnPos"];
    except:
        addAthleteOkBtnPos = {"x": 10, "y": 10};

    #try:
    #    events = config["events"];
    #except:
    #    events = { "50 fly":        {"x": 10, "y": 10},
    #               "50 back":       {"x": 10, "y": 10},
    #               "50 breast":     {"x": 10, "y": 10},
    #               "50 free":       {"x": 10, "y": 10},
    #               "100 fly":       {"x": 10, "y": 10},
    #               "100 back":      {"x": 10, "y": 10},
    #               "100 breast":    {"x": 10, "y": 10},
    #               "100 free":      {"x": 10, "y": 10},
    #               "100 im":        {"x": 10, "y": 10},
    #               "200 fly":       {"x": 10, "y": 10},
    #               "200 back":      {"x": 10, "y": 10},
    #               "200 breast":    {"x": 10, "y": 10},
    #               "200 free":      {"x": 10, "y": 10},
    #               "200 im":        {"x": 10, "y": 10},
    #               "400 im":        {"x": 10, "y": 10},
    #               "500 free":      {"x": 10, "y": 10},
    #               "1000 free":     {"x": 10, "y": 10},
    #             };

    # Start application
    startAppBtnPos = configureCursor(startAppBtnPos, "Start the application")
    if (startAppBtnPos == -1) return -1;

    # Athletes button
    athletesBtnPos = configureCursor(athletesBtnPos, "Click the athletes button")
    if (athletesBtnPos == -1) return -1;

    # Add new athlete
    addAthleteBtnPos = configureCursor(addAthleteBtnPos, "Add a new athlete")
    if (addAthleteBtnPos == -1) return -1;

    # Add new athlete ok button
    addAthleteOkBtnPos = configureCursor(addAthleteOkBtnPos, "Add a new athlete")
    if (addAthleteOkBtnPos == -1) return -1;

    #print("Configure event positions:\n");
    #for event in events:
    #    events[event] = configureCursor(events[event], "Event:");
    #    if (events[event] == -1) return -1;
    updates = {
        "startAppBtnPos": startAppBtnPos,
        "athletesBtnPos": athletesBtnPos,
        "addAthleteBtnPos": addAthleteBtnPos,
        "addAthleteOkBtnPos": addAthleteOkBtnPos}

    updateConfigFile(updates);
    print("Updated config file!");

    return 0;
