from General import *


AudioStream = {"Voice Call": 0, "System": 1, "Phone Ring": 2, "Music": 3,
                "Alarm": 4, "Notification": 5, "Bluetooth SCO": 6,
                "System Enforced": 7, "DTMF": 8, "TTS": 9}

# 4: Alarm 8: DTMF Tones 10: Accessibility Prompts 5: Notifications 2: Phone Ring 1: System 0: Voice Call 3: Music

# usage: media [subcommand] [options]
#        media dispatch KEY
#        media list-sessions
#        media monitor <tag>
#        media volume [options]
#
# media dispatch: dispatch a media key to the system.
#                 KEY may be: play, pause, play-pause, mute, headsethook,
#                 stop, next, previous, rewind, record, fast-forword.
# media list-sessions: print a list of the current sessions.
# media monitor: monitor updates to the specified session.
#                        Use the tag from list-sessions.
# media volume:  the options are as follows:
#                 --stream STREAM selects the stream to control, see AudioManager.STREAM_*
#                                 controls AudioManager.STREAM_MUSIC if no stream is specified
#
#
#                 --set INDEX     sets the volume index value
#                 --adj DIRECTION adjusts the volume, use raise|same|lower for the direction
#                 --get           outputs the current volume
#                 --show          shows the UI during the volume change
#         examples:
#                 adb shell media volume --show --stream 3 --set 11
#                 adb shell media volume --stream 0 --adj lower
#                 adb shell media volume --stream 3 --get


media = "adb shell media"


def change_volume_to(num: int):
    # num should be between [1,15]
    reported_command(f"{media} volume --set {num} --show")


def volume_down():
    reported_command(f"{media} volume --adj lower --show")


def volume_up():
    reported_command(f"{media} volume --adj raise --show")


def next_song():
    reported_command(f"{media} dispatch next")


def media_play():
    reported_command(f"{media} dispatch play")


def media_pause():
    reported_command(f"{media} dispatch pause")


def get_volume(stream=3):
    # "Voice Call": 0, "System": 1, "Phone Ring": 2, "Music": 3,
    # "Alarm": 4, "Notification": 5, "Bluetooth SCO": 6,
    # "System Enforced": 7, "DTMF": 8, "TTS": 9
    report = listed_command(f"{media} volume --stream {stream} --get")
    try:
        split = report[-1].split(" ")
        print(f"Current Volume of {IOHelper.keyOfValue(AudioStream, stream)} is {split[3]}")
        ask = AudioStream.values()
        return int(split[3])
    except IndexError:
        print("No Device is found.")
        return -1


def set_volume(vol: int, stream=3):
    reported_command(f"{media} volume --stream {stream} --set {vol} --show")