from .action import click_at_point
from .action import click_in_block
from .action import find_pic_inscreen
from .action import find_pic_andclick

from .action import pag

from .action import randint


def click_in_safe():
    click_in_block([(100, 340), 10, 10])
