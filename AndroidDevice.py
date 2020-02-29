from General import *


class RemoteDevice:
    def __init__(self, product="null", model="null", deviceIP="0.0.0.0:5555", transport_id=1,):
        self.product = product
        self.model = model
        self.IP = deviceIP.split(":")[0]
        self.port = deviceIP.split(":")[1]
        self.transport_id = transport_id

    def connect(self):
        reported_command(f"adb connect {self.IP}:{self.port}")

    def disconnect(self):
        reported_command(f"adb disconnect {self.IP}:{self.port}")

    def getIP(self):
        return f"{self.IP}:{self.port}"

    def toDict(self) -> dict:
        return {
            "product": self.product,
            "model": self.model,
            "IP": self.IP,
            "port": self.port,
            "transport_id": self.transport_id
        }


if __name__ == '__main__':
    device = RemoteDevice()
    print(device.transport_id)
    print(device.toDict())
