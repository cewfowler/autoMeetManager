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
def addAthlete(addAthletePos, athlete, team):
    [x, y] = getCoordinates(addAthletePos);

    pyautogui.moveTo(x, y, duration=0.1);
    pyautogui.click();
    sleep(0.5);

    # Get the athlete info
    [firstName, lastName] = athlete["name"].split(" ",1);
    id = athlete["id"];
    gender = athlete["gender"];

    printAthleteInfo(firstName, lastName, id, gender);

    pyautogui.write(lastName, interval=0.1);
    pyautogui.press('tab', interval=0.1);
    pyautogui.write(firstName, interval=0.1);

    tabToField(6);
    pyautogui.write(id, interval=0.1);

    # Gender field
    pyautogui.press('tab', interval=0.1);
    pyautogui.write(gender, interval=0.1);

    # Team field
    tabToField(3);
    pyautogui.write(team, interval=0.1);
    pyautogui.press('tab', interval=0.1);

    # OK btn
    tabToField(32);
    pyautogui.press('enter', interval=0.1);
