import socket, json

class GoveeLightDevice:
    sock, deviceIPAddress, devicePort = None, None, None
    def __init__(self, deviceIPAddress, devicePort = 4003):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.deviceIPAddress = deviceIPAddress
        self.devicePort = devicePort
    def setColor(self, red, green, blue, temp = 0):
        deviceRequest = {
            'msg': {
                'cmd': 'colorwc',
                'data': {
                    'color': {
                        'r': red,
                        'g': green,
                        'b': blue,
                        'colorTemInKelvin': temp
                    }
                }
            }
        }
        self.sock.sendto(bytes(json.dumps(deviceRequest), 'utf-8'), (self.deviceIPAddress, self.devicePort))

# TEMPORARY TESTS
print('running tests')
device1 = GoveeLightDevice('192.168.1.142')
device1.setColor(110, 110, 110)