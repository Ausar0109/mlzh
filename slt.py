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
        time.sleep(1)
        if isinstance(t1, tuple):
            break

    click3(zbx['window'], zbx['window'])
    time.sleep(2)  # 点击两次弹出宝箱

    if sikao:
        pig.moveTo(rand_choose(zbx['outwindow']), duration=2)
        sikaoshijian = 230 * sikao * randint(65, 135) / 100
        sikaoshijian = sikaoshijian // 1
        print('本次思考时间-----------【 %s 】' % sikaoshijian)

        transfer()
        time.sleep(sikaoshijian)

    click3(zbx['wupin1'], zbx['wupin2'], zbx[
           'zailaiyici'], zbx['kaishizhandou'])
    pig.moveTo(rand_choose(zbx['outwindow']), duration=1.5)

    if maitili:  # 买体力模块
        if isinstance(find_pic('liwuxiang'), tuple):
            find_pic_click('liwuxiang')
            find_pic_click('shouqu')
            find_pic_click('liwuxiang-guanbi')
            click3(zbx['zailaiyici'])

    print('本次运行时间:%s' % (datetime.now() - ts).seconds)
    time.sleep(5)
    transfer()

if __name__ == '__main__':
    while True:
        mainfunc(things='left2', huangou=0, maitili=True, sikao=0)

# 第一我没有红水
# 第二不动永远被动
# 第三 巨10 龙10 收益高
