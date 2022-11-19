
#import pyautogui
import win32api
import pyautogui
import time

print('MADDUS 1.0.12-E8 실행중, Made By Mado!')
print('\n\n프로그램이 시작되었어요!')
print('마우스 하를 누르면 F8이, 마우스 상을 누르면 ESC가 실행되요.')
while True:
    time.sleep(0.1)
    DC = win32api.GetAsyncKeyState(0x05)
    UC = win32api.GetAsyncKeyState(0x06)
    
    #print(click)
    if DC < 0:
        print('F8이 실행되었어요.')
        pyautogui.press('F8')

    if UC < 0:
        print('ESC가 실행되었어요.')
        pyautogui.press('ESC')
    