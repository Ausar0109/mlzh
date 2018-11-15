import pyautogui as pig
from random import randint, choice
import time
from datetime import datetime

pig.PAUSE = 1
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'


def click3(xy):
    pig.moveTo(xy, tween=pig.easeInQuad, duration=0.66)
    pig.click(pause=0.22)


def rand_choose(atuple, weight, hight):
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))

keyxy = (0, 0)
print("程序开始运行...")


pig.hotkey('ctrl','alt', 'a')
        
click3(rand_choose((keyxy[0] + 204, keyxy[1] + 125), 2, 2))
time.sleep(2)
pig.dragTo(rand_choose((keyxy[0] + 571, keyxy[1] + 456), 2, 2))
click3(rand_choose((keyxy[0] + 571, keyxy[1] + 456), 2, 2))
click3(rand_choose((keyxy[0] + 534, keyxy[1] + 478), 2, 2))

click3(rand_choose((keyxy[0] + 1282, keyxy[1] + 502), 2, 2))
pig.hotkey('ctrl', 'v')

 