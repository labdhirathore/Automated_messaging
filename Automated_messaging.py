# Automated Text Messaging

# Importing relevant Modules
import time
import pyautogui

# Let's do some CoDing!
def sendmessage():
    time.sleep(5)
    text = open('messages.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

sendmessage()




