import pyautogui as at
import time

at.hotkey("win" , "r")
at.write("https://www.youtube.com/" , interval=0.01)
at.press("enter")         
time.sleep(2)

