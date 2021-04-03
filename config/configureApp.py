import sys;
import pyautogui;
import json;
import cmd;
from adjustCursor import configureCursor;
from configUtility import loadStartingPos, resetContext;

# Reads config info
# Returns: config object or empty object if there is an error
def readConfigFile():
    try:
        with open('config/config.json', 'r') as f:
            config = json.load(f);
            f.close();

        return config;
    except:
        return [];


# Writes updated config info
#   updatedConfig: value to update
def updateConfigFile(updatedConfig):
    with open('config/config.json', 'w+') as f:
        json.dump(updatedConfig, f);
        f.close();

# Prompts the user to enter their team
#   team: the existing team name (or "" if there is none)
# Returns team name of -1 on too many failed attempts
def getTeam(team):
    accurateEntry = False;
    count = 0;

    while (not accurateEntry):
        if (team == ""):
            team = input("Enter the team name (the one used in the team field): ");
        yesOrNo = input("Team name: " + team + ". Is this correct? (Enter \'y\' for yes or \'n\' for no): ");
        if (yesOrNo == "y"):
            accurateEntry = True;
        elif (yesOrNo == "n"):
            team = "";
            count = 0;
        else:
            print("Sorry I didn't quite get that...");
            count += 1;

            if (count > 3):
                print("Sorry, too many failed attempts. Better luck next time.");
                return -1;
    return team;

# Configure all the mouse locations for the application
# Returns: 0 if config was successful, -1 otherwise
def configureMeetManager():
    config = readConfigFile();
    try:
        team = config["team"];
    except:
        team = "";
    team = getTeam(team);

    if (team == -1):
        return -1;

    [resetContext, startAppBtnPos, athletesBtnPos, addAthleteBtnPos] = loadStartingPos(config);

    resetContext["commandPromptToolbarPos"] = configureCursor(resetContext["commandPromptToolbarPos"],
        "First things first (warm up): Get the cursor over this screen (command prompt)");
    if (resetContext["commandPromptToolbarPos"] == -1):
        return -1;

    resetContext["commandPromptPos"] = configureCursor(resetContext["commandPromptPos"],
        "Now click the command prompt button on the toolbar (where you would click to minimize/maximize this screen)");
    if (resetContext["commandPromptPos"] == -1):
        return -1;

    print("Now adjust the cursor to be over the following functionality:");

    # Start application
    startAppBtnPos = configureCursor(startAppBtnPos, "Starting the application");
    if (startAppBtnPos == -1):
        return -1;

    # Athletes button
    athletesBtnPos = configureCursor(athletesBtnPos, "The athletes button/tab");
    if (athletesBtnPos == -1):
        return -1;

    # Add new athlete
    addAthleteBtnPos = configureCursor(addAthleteBtnPos, "The \"Add a new athlete\" button/tab")
    if (addAthleteBtnPos == -1):
        return -1;

    #print("Configure event positions:\n");
    #for event in events:
    #    events[event] = configureCursor(events[event], "Event:");
    #    if (events[event] == -1) return -1;

    updates = {
        "team": team,
        "resetContext": resetContext,
        "startAppBtnPos": startAppBtnPos,
        "athletesBtnPos": athletesBtnPos,
        "addAthleteBtnPos": addAthleteBtnPos,}

    updateConfigFile(updates);
    print("Updated config file!");

    return 0;
