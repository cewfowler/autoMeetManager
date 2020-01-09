import sys;
import pyautogui;

# OS can be 'linux' (Linux), 'win32' (Windows), 'darwin' (macOS)
os = sys.platform;
print("Operating system:", os);

width, height = pyautogui.size();
print("Screen size:", width, ",", height, "pixels");

if (os.startswith('darwin')):
    print("Running on MacOS system");
elif (os.startswith('win32')):
    print("Running on Windows32 system");
elif (os.startswith('linux')):
    print("Running on Linux system");

def main():
    # pyautogui.moveTo(x, y, duration in seconds);
    # Moves the mouse in a square starting from bottom right, clockwise
    pyautogui.moveTo(width/4, height*3/4, duration=0.25);
    pyautogui.moveTo(width/4, height/4, duration=0.25);
    pyautogui.moveTo(width*3/4, height/4, duration=0.25);
    pyautogui.moveTo(width*3/4, height*3/4, duration=0.25);

if __name__ == '__main__':
    main();
