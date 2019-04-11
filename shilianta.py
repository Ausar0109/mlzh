from mlzhlc import find_pic_inscreen, find_pic_andclick
import time

def shilianta_action_after_findpic(shangdian=False):
    find_pic_andclick('战斗胜利闪电', (-20,5))
    find_pic_andclick('战斗胜利红水', (10,10))
    find_pic_andclick('确认其它道具')
    find_pic_andclick('确认刻印石')
    find_pic_andclick('确认彩虹怪')
    find_pic_andclick('世界地图', (-318, -100))
    find_pic_andclick('开始战斗')
    print('完成了一次检测~~, 休息一会')
    time.sleep(10)

if __name__ == '__main__':
    while True:
        shilianta_action_after_findpic()