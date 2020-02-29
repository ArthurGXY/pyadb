from General import *
from InputSim import *
import time


def wait(sec):
    time.sleep(sec)


def _next():
    tap(1700, 1000)


def esc():
    tap(170, 70)


def confirm():
    tap(1160, 888)


def skip_dialog():
    tap(2100, 100)
    wait(0.5)
    tap(1425, 100)
    wait(0.5)
    confirm_messageBox()


def confirm_messageBox():
    tap(1350, 675)


def collect():
    tap(2140, 400)
    wait(0.8)
    tap(1800, 235)
    wait(0.5)
    tap(1130, 879)


def option():
    tap(2150, 85)
    tap(1350, 475)


if __name__ == '__main__':
    # _next()
    # esc()
    # confirm()
    option()
