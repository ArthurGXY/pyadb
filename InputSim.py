from General import *
import os

key_event = "adb shell input keyevent"
shell_input = "adb shell input"


def play_pause():
    reported_command(f"{key_event} 85")


def tap(x: int, y: int):
    reported_command(f"{shell_input} tap {x} {y}")


if __name__ == '__main__':
    tap(1700, 1000)