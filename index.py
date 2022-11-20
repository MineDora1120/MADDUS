
#import pyautogui
import win32api
import pyautogui
import time
import os
import json

filepath = 'config.json'

if os.path.isfile(filepath) == False:
    data = '''{
        "up": {
            "type": "press",
            "firstkey": "F6",
            "secondkey": "none"
            },
        "down": {
            "type": "hotkey",
            "firstkey": "ctrl",
            "secondkey": "c"
            },
        "log": "true"
        }
    '''
    file = open(filepath, 'w')
    print(data, file=file)
    file.close()

with open(filepath, 'r') as f:
    data = json.load(f)
    
    DPS = data['down']['firstkey']
    DPSS = (f"{data['down']['firstkey']}+{data['down']['secondkey']}")

    UPS = data['up']['firstkey']
    UPSS = (f"{data['up']['firstkey']}+{data['up']['secondkey']}")

    print('MADDUS 2.0.14 실행중, Made By Mado!')
    print('\n\n프로그램이 시작되었어요!')
    down = (f'{DPS}' if data['down']['type'] == 'press' else f'{DPSS}')
    up = (f'{UPS}' if data['up']['type'] == 'press' else f'{UPSS}')

    print(f'마우스 하를 누르면 {down}이(가) 실행되고, 마우스 상을 누르면 {up}이(가) 실행되요.')
    if data['log'] == "true":
        print('\n마우스의 위, 아래 버튼을 클릭할때 마다 로그가 발생해요! 이 설정은 프로그램이 있는 config.json에서 끌 수 있어요.')
    else:
        print('\n마우스의 위, 아래 버튼을 클릭할때 마다 로그가 나오지 않아요. 이 설정은 프로그램이 있는 config.json에서 켤 수 있어요.')

    while True:
        time.sleep(0.1)
        DC = win32api.GetAsyncKeyState(0x05)
        UC = win32api.GetAsyncKeyState(0x06)
        
        #print(click)
        if DC < 0:
            if data['log'] == "true": print(f'마우스 아래버튼을 눌러, {down}이(가) 실행되었어요!')
            if data['down']['type'] == 'press':
                pyautogui.press(f"{data['down']['firstkey']}")
            else:
                pyautogui.hotkey(f"{data['down']['firstkey']}", f"{data['down']['secondkey']}")

        if UC < 0:
            if data['log'] == "true": print(f'마우스 위버튼을 눌러, {up}이(가) 실행되었어요!')
            if data['up']['type'] == 'press':
                pyautogui.press(f"{data['up']['firstkey']}")
            else:
                pyautogui.hotkey(f"{data['up']['firstkey']}", f"{data['up']['secondkey']}")
    