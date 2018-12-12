import pyautogui as pig
from random import randint, choice
import time
import json
from mlzhlc import rand_choose, click3, transfer, find_pic_click, find_pic
from datetime import datetime

pig.PAUSE = 0.5
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'
keyxy = (0, 0)

with open(jdpath + 'zbx.aa', 'r') as f:
    zbx = json.load(f)


def mainfunc(things='left', huangou=True, maitili=False, sikao=True):
    ts = datetime.now()
    jiancecishu = 0
    while True:
        t1 = pig.locateCenterOnScreen(jdpath + 'dwpic/shengli.png')
        time.sleep(5)
        if isinstance(t1, tuple):
            break
        t2 = pig.locateCenterOnScreen(jdpath + 'dwpic/siwang.png')
        time.sleep(2)
        if isinstance(t2, tuple):
            transfer()
            click3(zbx['bufuhuo'], zbx['window'])  # 不复活 点击window确认
            click3(zbx['zailaiyici'], zbx['diyihaoyou'],zbx['kaishizhandou'])  # 点击再来一次 进入复活准备页面
            pig.moveTo(rand_choose(zbx['outwindow']))
            break

    click3(zbx['window'], zbx['window'])
    time.sleep(2)  # 点击两次弹出宝箱

    if things == 'left':
        click3(zbx['fw-left'])
        click3(zbx['zailaiyici'])
    elif things == 'left2':
        click3(zbx['fw-left'])
        pig.moveTo(rand_choose(zbx['fw-sold']), pause=0.5)  # 给缓冲时间
        click3(zbx['fw-sold'])
    else:
        click3(zbx['fw-right'])

    click3(zbx['wupin1'], zbx['wupin2'])
    click3(zbx['zailaiyici'], zbx['diyihaoyou'],zbx['kaishizhandou'])
    pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)


    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(5)
    transfer()

if __name__ == '__main__':
    while True:
        mainfunc(things='left2')
