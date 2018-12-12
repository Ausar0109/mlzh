import pyautogui as pig
from random import randint, choice
import time
import json
from datetime import datetime
import pyperclip

pig.PAUSE = 0.5
# 全局阻断0.5
pig.FAILSAFE = True
# 可以打断
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'
# 文件位置固定死
keyxy = (0, 0)
# 窗口位置固定死

with open(jdpath + 'zbx.aa', 'r') as f:
    zbx = json.load(f)


def ppaste(astr):
    '''Recreated typwrite for ###supportting chinese-lang'''
    pyperclip.copy(astr)
    pig.hotkey('ctrl', 'v')


def rand_choose(zuobiao_pack):
    '''zuobiao_pack : [(x,y),weight,hight]'''
    atuple, weight, hight = zuobiao_pack[0], zuobiao_pack[1], zuobiao_pack[2]
    x = keyxy[0] + atuple[0] + randint(0, weight)
    y = keyxy[1] + atuple[1] + randint(0, hight)
    return (x, y)


def click3(*zuobiao_pack):
    '''*zuobiao_pack : zuobiao_pack1, zuobiao_pack2  '''
    for i in range(len(zuobiao_pack)):
        _xy = zuobiao_pack[i]
        xy = rand_choose(_xy)
        pig.moveTo(xy, tween=pig.easeInQuad, duration=0.75)
        pig.click(pause=0.15)
        pig.moveTo(xy, pause=0.2)


def find_pic(PicName, timesleep=2):
    time.sleep(timesleep)
    PicTuple = pig.locateCenterOnScreen(
        jdpath + 'dwpic/' + PicName + '.png', grayscale=True)
    if isinstance(PicTuple, tuple):
        return PicTuple


def find_pic_click(PicName, timesleep=2):
    time.sleep(timesleep)
    PicTuple = pig.locateCenterOnScreen(
        jdpath + 'dwpic/' + PicName + '.png', grayscale=True)
    if isinstance(PicTuple, tuple):
        click3([(PicTuple[0] - 3, PicTuple[1] - 3), 6, 6])


def ccenter(input_str):
    print(input_str)
    click3(zbx['QQ-blank'])
    ppaste(input_str)
    time.sleep(2)
    find_pic_click('fasong')


def transfer():
    pig.hotkey('ctrl', 'alt', 'a')
    click3(zbx['window'], zbx['jietu-queding'], zbx['QQ-blank'])
    pig.hotkey('ctrl', 'v')


def tfind_pic_click(PicName):
    while True:
        if isinstance(find_pic(PicName), tuple):
            break
        time.sleep(2)
    find_pic_click(PicName)
