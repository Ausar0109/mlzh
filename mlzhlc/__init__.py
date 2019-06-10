from .action import click_at_point
from .action import click_in_block
from .action import click_in_block2
from .action import ppaste

from .action import find_pic_inscreen
from .action import find_pic_andclick
from .action import save_screen

from .action import pag, time

from .action import randint


def click_in_safe(pause=0):
    time.sleep(pause)
    click_in_block([(83, 342), 28, 4])
