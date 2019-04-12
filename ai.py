from mlzhlc import *
import time


def refresh_screen():
    while True:
        click_in_safe()
        if find_pic_inscreen('战斗图标'):
            break


def get_in():
    find_pic_andclick('战斗图标')
    while True:
        find_pic_andclick('关闭限时商品')
        find_pic_andclick('关闭限时道具')
        find_pic_andclick('关闭限时道具确定')
        if find_pic_inscreen('卡伊洛斯地下城'):
            break


def get_out():
    for i in range(randint(4, 6)):
        pag.press('esc', pause=0.5)
    find_pic_andclick('不结束游戏')


def dixiacheng_loop():
    refresh_screen()
    get_in()

    find_pic_andclick('卡伊洛斯地下城')
    find_pic_andclick('龙之地下城', pause=2)
    find_pic_andclick('龙之第十层', (250, 1))
    find_pic_andclick('开始战斗')

    while True:
        time.sleep(randint(10, 30))
        find_pic_andclick('火吸', (-450, 2))
        find_pic_andclick('复活图标', (200, 5))

        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('战斗胜利红水')

        find_pic_andclick('获得符石道具')
        find_pic_andclick('确认其它道具')
        find_pic_andclick('确认刻印石')

        find_pic_andclick('回城')
        find_pic_andclick('重新发送')

        if find_pic_inscreen('战斗图标'):
            break
        if find_pic_inscreen('商店图标'):
            break

    get_out()


def jingjichang_loop():
    refresh_screen()
    get_in()

    find_pic_andclick('竞技场图标')
    find_pic_andclick('普通竞技场')

    if find_pic_inscreen('竞技场挑战'):  # 挑战图标完好，说明没有挑战者，进入 竞技场对战
        find_pic_andclick('竞技场对战')
        find_pic_andclick('竞技场刷新', pause=3)
        find_pic_andclick('竞技场翅膀')
        find_pic_andclick('开始战斗')

    else:  # 说明有挑战者，进入 竞技场挑战
        find_pic_andclick('竞技场对战', (1, 75))

        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i))
            find_pic_andclick('挑战者未备')
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break
        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)
        pag.scroll(clicks=-100)
        for i in [40, 95, 140, 190, 250]:
            find_pic_andclick('挑战者翅膀', (195, i))
            find_pic_andclick('挑战者未备')
            if find_pic_inscreen('开始战斗'):
                find_pic_andclick('开始战斗')
                break

    while True:
        time.sleep(randint(10, 30))
        click_in_safe()

        find_pic_andclick('一速', (-450, 2))
        find_pic_andclick('战斗胜利闪电')
        find_pic_andclick('竞技场名誉')
        find_pic_andclick('关闭竞技场')
        find_pic_andclick('竞技场返回')

        if find_pic_inscreen('战斗图标'):
            break
        if find_pic_inscreen('商店图标'):
            break

        click_in_safe()

    get_out()


def shangdian_loop():
    while True:
        click_in_safe()
        time.sleep(2)
        find_pic_andclick('战斗图标', (-55, -165))
        if find_pic_inscreen('商店信息图标'):
            find_pic_andclick('商店信息图标', (-70, 0))
            break

    def find_target_in_fourblock(target):
        for i in [90, 150, 210, 270]:
            find_pic_andclick('魔法商店里面', (0, i))
            for k in target:
                if find_pic_inscreen(k):
                    find_pic_andclick('商店购买')
                    find_pic_andclick('商店购买2')
                    find_pic_andclick('购买确认')

    for i in range(4):
        find_target_in_fourblock(['两星魔灵', '神秘召唤书', '商店刻印石'])
        find_pic_andclick('魔法商店里面', (0, 100))
        pag.scroll(clicks=-1)
        pag.scroll(clicks=-1)

    for i in range(randint(3, 5)):
        pag.press('esc', pause=0.5)
    find_pic_andclick('不结束游戏')

if __name__ == '__main__':
    click_in_safe()
    while True:

        dixiacheng_loop()
        dixiacheng_loop()
        jingjichang_loop()
        shangdian_loop()

        time.sleep(randint(3, 6) * 2)
