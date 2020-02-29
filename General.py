import os
import IOHelper
from AndroidDevice import RemoteDevice


class ADBError(Exception):
    pass


def reported_command(command: str):
    lines = listed_command(command)
    for line in lines:
        print(line)


def get_devices():
    report = listed_command("adb devices -l")
    devices = []
    if len(report) > 1:
        for lines in report[1:]:
            if lines != "":
                deviceIP = IOHelper.until_1st_space(lines)
                info = IOHelper.after_1st_space(lines).split(" ")
                product = info[1].split(":")[1]
                model = info[2].split(":")[1]
                tp_id = info[1].split(":")[1]
                devices.append(
                    RemoteDevice(deviceIP=deviceIP,
                                 product=product,
                                 model=model,
                                 transport_id=tp_id)
                )
    return devices


def listed_command(command: str):
    print(command)
    out = os.popen(command)
    res = out.read()
    lines = []
    for line in res.splitlines():
        lines.append(line)
    return lines


def screen_shot(remote_dir=r"/sdcard", file_name=r"/screenshot.png", save_dir=r"D:\adb_screenshots"):
    reported_command(f"adb shell /system/bin/screencap -p {remote_dir}{file_name}")
    reported_command(f"adb pull {remote_dir}{file_name} {save_dir}")
    return save_dir + file_name


def wireless_connect(IP: str, port="5555"):
    reported_command(f"adb connect {IP}:{port}")

