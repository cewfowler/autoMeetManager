import sys;
import pyautogui;
import json;
import readchar;
from adjustCursor import configureCursor

# Reads config info
#   Returns config object or empty object if there is an error
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
def configureMeetManager():
    config = readConfigFile();

    try:
        startAppPos = config["startAppPos"];
    except:
        startAppPos = {"x": 10, "y": 10};

    try:
        athletesPos = config["athletesPos"];
    except:
        athletesPos = {"x": 10, "y": 10};

    try:
        addAthletePos = config["addAthletePos"];
    except:
        addAthletePos = {"x": 10, "y": 10};

    try:
        addAthleteOkPos = config["addAthleteOkPos"];
    except:
        addAthleteOkPos = {"x": 10, "y": 10};

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
    startAppPos = configureCursor(startAppPos, "Start the application")
    if (startAppPos == -1) return -1;

    # Athletes button
    athletesPos = configureCursor(athletesPos, "Click the athletes button")
    if (athletesPos == -1) return -1;

    # Add new athlete
    addAthletePos = configureCursor(addAthletePos, "Add a new athlete")
    if (addAthletePos == -1) return -1;

    #print("Configure event positions:\n");
    #for event in events:
    #    events[event] = configureCursor(events[event], "Event:");
    #    if (events[event] == -1) return -1;
    updates = {
        "startAppPos": startAppPos,
        "athletesPos": athletesPos,
        "addAthletePos": addAthletePos,
        "addAthleteOkPos": addAthleteOkPos}

    updateConfigFile(updates);
    print("Updated config file!");

    return 0;
