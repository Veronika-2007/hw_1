#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath():
        move_right()
    while not wall_is_beneath():
        move_right()
        move_down()
        move_right()
        move_left()
        move_down(2)
    while wall_is_beneath():
        move_right()
    while wall_is_above():
        move_down(1)







if __name__ == '__main__':
    run_tasks()
