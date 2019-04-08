from mlzhlc import find_pic_inscreen, find_pic_andclick
import time

def dixiacheng_action_after_findpic(shangdian=False):
    find_pic_andclick('复活图标', (200,5)) #

    find_pic_andclick('战斗胜利闪电') #
    find_pic_andclick('战斗胜利红水')

    find_pic_andclick('获得符石道具')
    find_pic_andclick('确认其它道具')
    find_pic_andclick('确认刻印石')

    find_pic_andclick('世界地图', (-318, -100)) #
    find_pic_andclick('开始战斗') #
    

    print('完成了一次检测~~, 休息一会')
    time.sleep(8*60)
    
    if shangdian:
    	find_pic_andclick('礼物箱图标')
    	find_pic_andclick('收取礼物箱闪电')
    	find_pic_andclick('关闭礼物箱')
    	find_pic_andclick('战斗准备', (-200, -100))

if __name__ == '__main__':
    while True:
        dixiacheng_action_after_findpic()