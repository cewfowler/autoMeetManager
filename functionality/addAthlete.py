import pyautogui;
from config.adjustCursor import getCoordinates;

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
def addAthlete(addAthletePos, athlete, teamPos, okPos):
    [addAthleteX, addAthleteY] = getCoordinates(addAthletePos)
    [teamX, teamY] = getCoordinates(teamPos)
    [okX, okY] = getCoordinates(okPos);

    pyautogui.moveTo(addAthleteX, addAthleteY, duration=0.1);
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

    pyautogui.press('tab', interval=0.1);
    pyautogui.press('tab', interval=0.1);
    pyautogui.press('tab', interval=0.1);
    pyautogui.press('tab', interval=0.1);
    pyautogui.press('tab', interval=0.1);
    pyautogui.write(id, interval=0.1);

    pyautogui.moveTo(teamX, teamY, duration=0.1);
    pyautogui.write("FCSD-FL", interval=0.1);
    pyautogui.press('tab', interval=0.1);

    pyautogui.moveTo(okX, okY, duration=0.1);
    pyautogui.click();
