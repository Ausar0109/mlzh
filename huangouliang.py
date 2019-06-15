from mlzhlc import *
import time


def huangouliang(num=15):
    ysj = find_pic_inscreen('右上角')
    ysj = ysj.left + ysj.width / 2, ysj.top + ysj.height / 2

    pxy = find_pic_inscreen('左下角')
    pxy = pxy.left + pxy.width / 2, pxy.top + pxy.height / 2

    for i in range(num):
        pag.click(ysj, duration=0.5, pause=0.11)
        pag.dragTo(pxy, duration=0.5, pause=0.11)

    find_pic_andclick('空白格子', (-250, 0))
    find_pic_andclick('空白格子', (-107, 0))
    find_pic_andclick('空白格子', (-177, 40))

    find_pic_andclick('黑色青蛙', (-180, 0))
    find_pic_andclick('黑色青蛙', (-60, 0))
    find_pic_andclick('黑色青蛙', (-120, 0))


def daigouliang(shangdian=True):
    # save_screen()
    click_in_safe()
    click_in_safe()

    find_pic_andclick('战斗胜利红水', (-177, 110), 0, 0)
    find_pic_andclick('战斗胜利红水', (-177, 150), 0, 0)
    find_pic_andclick('获得符石道具', (-115, 0), 0, 0)
    find_pic_andclick('确认卖出符文', (0, 0), 0, 0)

    find_pic_andclick('世界地图', (-318, -100), 0, 0)

    if shangdian:
        if find_pic_inscreen('商店图标'):
            find_pic_andclick('礼物箱图标')
            find_pic_andclick('收取礼物箱闪电')
            find_pic_andclick('关闭礼物箱')
            find_pic_andclick('世界地图', (-318, -100))

    if find_pic_inscreen('开始战斗'):
        huangouliang()
        find_pic_andclick('开始战斗')
        pass


if __name__ == '__main__':
    # huangouliang()
    while True:
        daigouliang(0)
