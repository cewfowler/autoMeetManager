import pyautogui;
from config.adjustCursor import getCoordinates,tabToField;

# Print an athletes info (for testing)
#   firstName: first name
#   lastName: last name
#   id: ID #
#   gender: gender (male or female)
def printAthleteInfo(firstName, lastName, id, gender):
    print("Athlete: " + lastName + ", " + firstName + "\n");
    print("\tID: " + id + "\n");
    print("\tGender: " + gender + "\n\n");


# Add new athletes into the system
#   addAthletePos: The position of the add athlete button on the screen
#   athletes: The athletes and their information
#   team: the new athlete's team
#   dur: the duration of moving/clicking with pyautogui
def addAthlete(addAthletePos, athlete, team, dur):
    [x, y] = getCoordinates(addAthletePos);

    pyautogui.moveTo(x, y, duration=dur);
    pyautogui.click();
    sleep(0.5);

    # Get the athlete info
    [firstName, lastName] = athlete["name"].split(" ",1);
    id = athlete["id"];
    gender = athlete["gender"];

    printAthleteInfo(firstName, lastName, id, gender);

    pyautogui.write(lastName, interval=dur);
    pyautogui.press('tab', interval=dur);
    pyautogui.write(firstName, interval=dur);

    tabToField(6, dur);
    pyautogui.write(id, interval=dur);

    # Gender field
    pyautogui.press('tab', interval=dur);
    pyautogui.write(gender, interval=dur);

    # Team field
    tabToField(3, dur);
    pyautogui.write(team, interval=dur);
    pyautogui.press('tab', interval=dur);

    # OK btn
    tabToField(32, dur);
    pyautogui.press('enter', interval=dur);
