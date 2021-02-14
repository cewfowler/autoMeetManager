import pyautogui;

# Add new athletes into the system
#   addAthletePos: The position of the add athlete button on the screen
#   athletes: The athletes and their information
def addAthlete(addAthletePos, athletes):
    width, height = pyautogui.size();
    x = addAthletePos["x"];
    y = addAthletePos["y"];

    for athlete in athletes:
        pyautogui.moveTo(width * x/100, height * (100 - y)/100, duration=0.1);
        pyautogui.click();
