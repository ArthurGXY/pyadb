import os
from menu import do_menu

SSID = ''
CON = ''
DISCON = 'dis'

REMOTE = r'/sdcard/netease/cloudmusic/music'
LOCAL = r'D:\CloudMusic'
IP_PREFIX = r'192.168.0.'


def reported_command(command: str):
    print(command)
    out = os.popen(command)
    res = out.read()
    lines = []
    for line in res.splitlines():
        lines.append(line)
        print(line)
    return lines





def use_wireless():
    # restart tcp port
    os.system("adb tcpip 5555")
    phone_one = IP_PREFIX + input('IP Address of phone 1\n')
    phone_two = IP_PREFIX + input('IP Address of phone 2\n')
    connect(phone_one)
    pull_phone()
    # adb_wireless_disconnect()
    # adb_wireless_connect(phone_two)


def pull_phone():
    reported_command(f"adb pull {REMOTE} {LOCAL}")


def reset_connection():
    reported_command("adb disconnect")
    reported_command("adb kill-server")


if __name__ == '__main__':
    reset_connection()
    print("\n当前WIFI信息：")
    WIFI_INFO = reported_command('netsh WLAN show interfaces')
    choice = do_menu(f"Change IP Prefix? Current One is \"{IP_PREFIX}\"", ["Yes", "No"])
    if choice == 1:
        IP_PREFIX = input("Input a new one.")
    use_wireless()
