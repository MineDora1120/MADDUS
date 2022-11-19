
#import pyautogui
import win32api
import pyautogui
import time

print('MADDUS 1.0.12-CV 실행중, Made By Mado!')
print('\n\n프로그램이 시작되었어요!')
print('마우스 하를 누르면 붙혀넣기가, 마우스 상을 누르면 복사가 되요.')
while True:
    time.sleep(0.1)
    DC = win32api.GetAsyncKeyState(0x05)
    UC = win32api.GetAsyncKeyState(0x06)
    
    #print(click)
    if DC < 0:
        print('붙혀넣어졌어요,')
        pyautogui.hotkey('ctrl', 'v')

    if UC < 0:
        print('복사 되었어요!')
        pyautogui.hotkey('ctrl', 'c')
    