import pyautogui as pig
from random import randint, choice
import time
import json
from datetime import datetime

pig.PAUSE = 0.5
pig.FAILSAFE = True
jdpath = 'C:/Users/cheng.lu/Desktop/mlzh/'
keyxy = (0, 0)

with open(jdpath + 'zbx.aa', 'r') as f:
    zbx = json.load(f)


def rand_choose(zuobiao_pack):
    atuple, weight, hight = zuobiao_pack[0], zuobiao_pack[1], zuobiao_pack[2]
    return (atuple[0] + randint(0, weight), atuple[1] + randint(0, hight))


def click3(*zuobiao_pack):
    for i in range(len(zuobiao_pack)):
        _xy = zuobiao_pack[i]
        xy = rand_choose(_xy)
        pig.moveTo(xy, tween=pig.easeInQuad, duration=1)
        pig.click(pause=0.3)
        pig.moveTo(xy, pause=0.2)


def transfer(pptime=2):
    pig.hotkey('ctrl', 'alt', 'a')
    click3(zbx['window'], zbx['jietu-queding'], zbx['QQ-blank'])
    time.sleep(pptime)
    pig.hotkey('ctrl', 'v')


def mainfunc(things='left', huangou=True, maitili=False, sikao=True):
    ts = datetime.now()
    jiancecishu = 0
    while True:
        t1 = pig.locateCenterOnScreen(jdpath + 'dwpic/shengli.png')
        time.sleep(1.5)
        if isinstance(t1, tuple):
            break
        t2 = pig.locateCenterOnScreen(jdpath + 'dwpic/siwang.png')
        time.sleep(1.5)
        if isinstance(t2, tuple):
            transfer()
            click3(zbx['bufuhuo'], zbx['window'])  # 不复活 点击window确认
            click3(zbx['zailaiyici'], zbx['kaishizhandou'])  # 点击再来一次 进入复活准备页面
            pig.moveTo(rand_choose(zbx['outwindow']))
            break

        jiancecishu += 1
        if jiancecishu % 200 == 0:
            transfer()

    click3(zbx['window'], zbx['window'])  # 点击两次弹出宝箱

    if sikao:
        pig.moveTo(rand_choose(zbx['outwindow']), duration=2)
        sikaoshijian = 230 * sikao * randint(65, 135) / 100
        sikaoshijian = sikaoshijian // 1
        print('本次思考时间-----------【 %s 】' % sikaoshijian)

        transfer()
        time.sleep(sikaoshijian)

    click3(zbx['fw-right'])
    click3(zbx['wupin1'], zbx['wupin2'], zbx['zailaiyici'])  # 搜寻物品确认按钮
    pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(3)
    transfer()

if __name__ == '__main__':
    while True:
        mainfunc(things='lc', huangou=False, maitili=False, sikao=0.01)

# 第一我没有红水
# 第二不动永远被动
# 第三 巨10 龙10 收益高
