import pyautogui as pa
import time


pa.PAUSE = 1

pa.press("win")
pa.write("chrome")
pa.press("enter")

pa.write("gmail.com")
pa.press("enter")
time.sleep(3)
pa.click(2652, 258)