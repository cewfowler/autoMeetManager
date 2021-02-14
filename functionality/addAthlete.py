import pyautogui;

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
def addAthlete(addAthletePos, athletes):
    width, height = pyautogui.size();
    x = addAthletePos["x"];
    y = addAthletePos["y"];

    pyautogui.moveTo(width * x/100, height * (100 - y)/100, duration=0.1);
    pyautogui.click();
    sleep(0.5);

    for athlete in athletes:
        # Get the athlete info
        [firstName, lastName] = athlete["name"].split(" ",1);
        id = athlete["id"];
        gender = athlete["gender"];

        printAthleteInfo(firstName, lastName, id, gender)

        pyautogui.write(lastName, interval=0.1);
        pyautogui.press('tab', interval=0.1);
        pyautogui.write(firstName, interval=0.1);
