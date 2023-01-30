import pyautogui
import time
print(pyautogui.position())
count=0
a=pyautogui.position()
while True:
    pyautogui.moveTo(a)
    time.sleep(0.5)
    pyautogui.click(a)
    pyautogui.hotkey('enter')
    count+=1
    if count==10:
        break
