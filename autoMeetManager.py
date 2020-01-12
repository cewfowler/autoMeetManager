import sys;
import pyautogui;

# Get OS
os = sys.platform;
print("Operating system:", os);

# Get screen width + height
width, height = pyautogui.size();
print("Screen size:", width, ",", height, "pixels");

# Acceptable OS's are 'linux' (Linux), 'win32' (Windows), 'darwin' (macOS)
if (os.startswith('darwin')):
    print("Running on MacOS system");
elif (os.startswith('win32')):
    print("Running on Windows32 system");
elif (os.startswith('linux')):
    print("Running on Linux system");
else:
    print("System not recognized. Please try again on a Linux, Windows32, or MacOS system.");

def main():
    # pyautogui.moveTo(x, y, duration in seconds);
    # Moves the mouse in a square starting from bottom right, clockwise
    pyautogui.moveTo(width/4, height*3/4, duration=0.25);
    pyautogui.moveTo(width/4, height/4, duration=0.25);
    pyautogui.moveTo(width*3/4, height/4, duration=0.25);
    pyautogui.moveTo(width*3/4, height*3/4, duration=0.25);

if __name__ == '__main__':
    main();
