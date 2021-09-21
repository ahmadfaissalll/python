import time
import re
import pyautogui
import keyboard
import sys

def get_current_time():
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    current_time = f"{hour}{minute}"
    return current_time

current_time = list(get_current_time())


if len(current_time) == 3:
    current_time.insert(2,'0')

a,b,c,d = current_time

print(f'\t\t\tProgram opened at {a}{b}:{c}{d}')

print("Note: gunakan format 24 jam!")

timeInput = input('Deadline: (hour:min) ')


if len(timeInput) > 5:
    print('\ninput lebih dari 5 character')
    sys.exit()

x = re.split(':', timeInput)
x = "".join(x)

try:
    x = int(x)

except ValueError:
    print('\ninput tidak valid!!! hanya menerima angka integer'.upper())
    sys.exit()


calculate = x - int(get_current_time())

time.sleep(calculate*60)

print('\nselesai')

pyautogui.keyDown('winleft')
pyautogui.press('r')
pyautogui.keyUp('winleft')

time.sleep(0.01)

pyautogui.write(list("notepad"))
pyautogui.press("enter")
time.sleep(0.8)

a,b,c,d = str(x)

keyboard.write(f'Deadline reached {a}{b}:{c}{d}')
