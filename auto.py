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
        
        if isinstance(t2, tuple):
            transfer()
            click3(zbx['bufuhuo'], zbx['window'])  # 不复活 点击window确认
            click3(zbx['zailaiyici'], zbx['kaishizhandou'])  # 点击再来一次 进入复活准备页面
            pig.moveTo(rand_choose(zbx['outwindow']))
            break

        jiancecishu += 1
        if jiancecishu % 201 == 0:
            transfer()

    click3(zbx['window'], zbx['window'])
    time.sleep(2)  # 点击两次弹出宝箱

    if sikao:
        pig.moveTo(rand_choose(zbx['outwindow']), duration=2)
        sikaoshijian = 230 * sikao * randint(65, 135) / 100
        sikaoshijian = sikaoshijian // 1
        print('本次思考时间-----------【 %s 】' % sikaoshijian)

        transfer()
        time.sleep(sikaoshijian)

    if things == 'left':
        click3(zbx['fw-left'])
        click3(zbx['zailaiyici'])
    elif things == 'left2':
        click3(zbx['fw-left'])
        pig.moveTo(rand_choose(zbx['fw-sold']), pause=0.5)  # 给缓冲时间
        click3(zbx['fw-sold'])
    else:
        click3(zbx['fw-right'])

    click3(zbx['wupin1'], zbx['wupin2'], zbx['zailaiyici'])
    pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)

    if maitili:  # 买体力模块
        if isinstance(find_pic('liwuxiang'),tuple):
            find_pic_click('liwuxiang')
            find_pic_click('shouqu')
            find_pic_click('liwuxiang-guanbi')
            click3(zbx['zailaiyici'])

    if huangou:  # 换狗粮模块
        click3(zbx['haoyou'])  # 用来补充弹出换狗粮页面的操作
        time.sleep(2)
        if isinstance(pig.locateCenterOnScreen(jdpath + 'dwpic/yiman.png'), tuple):
            transfer()
            click3(zbx['shangdian3'])
            for i in range(huangou):
                pig.moveTo(rand_choose(zbx['move-right']))
                pig.dragTo(rand_choose(zbx['move-left']),
                           duration=randint(5, 15) / 12, button='left')
            time.sleep(2)
            click3(zbx['w1'], zbx['w2'], zbx['w3'])
            click3(zbx['m1'], zbx['m2'], zbx['m3'])
            click3(zbx['kaishizhandou'])
            pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(5)
    transfer()

if __name__ == '__main__':
    while True:
        mainfunc(things='right', huangou=0, maitili=True, sikao=0.01)

# 第一我没有红水
# 第二不动永远被动
# 第三 巨10 龙10 收益高
