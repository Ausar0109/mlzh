from pyautogui import screenshot
from random import randint

mlpath = 'C:/Users/cheng.lu/Desktop/mlzh/'

screenshot().save(mlpath + 'dwpic/%s.png'%randint(1,9999))
