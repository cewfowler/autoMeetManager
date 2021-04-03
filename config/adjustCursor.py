import sys;
import pyautogui;
import json;
import readchar;

# Allows user to update cursor location for config
#   x: starting x position
#   y: starting y position
#   Returns new x and y positions, or -1 if process cancelled
#   newX: adjusted x position
#   newY: adjusted y position
# Returns: the new x and y positions
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


# Allow user to select new coordinate values
#   vals: The original coordinate values
#   msg: The message to display to the user
# Returns: the new x and y vals saved as the JSON position
def configureCursor(vals, msg):
    # Add new athlete
    x = vals["x"];
    y = vals["y"];

    print(msg + ":\n")
    newX,newY = adjustCursor(x,y);
    if (newX == -1 and newY == -1):
        print("Update config cancelled.")
        return -1;

    vals["x"] = newX;
    vals["y"] = newY;

    return vals;


# Get the x and y cooredinates for the screen given the JSON position
#   position: the JSON position
# Returns: the x and y position on the screen
def getCoordinates(position):
    width, height = pyautogui.size();

    posX = width * position["x"]/100;
    posY = height * (100 - position["y"])/100;

    return [posX, posY];

def tabToField(numTabs):
    for i in range(1, numTabs):
        pyautogui.press('tab', interval=0.1);
