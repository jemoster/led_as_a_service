import requests
import json

__author__ = 'Joe'


class TricolorLED:
    """An interface for controlling a Tricolor LED over the serial port"""

    def __init__(self, address, access_token):
        self.address = address
        self.access_token = access_token
        self.s = requests.Session()

        self._cal = {
            'red': 1.0,
            'green': 0.3,
            'blue': 0.2,
        }

    def raw(self, red, green, blue):
        data = {
            'red': int(red),
            'green': int(green),
            'blue': int(blue),
        }
        print json.dumps(data)
        self.s.post(self.address, data={'access_token': self.access_token, 'params': json.dumps(data)})

    def rgb(self, red, green, blue):
        data = {
            'red': int(red*self._cal['red']),
            'green': int(green*self._cal['green']),
            'blue': int(blue*self._cal['blue']),
        }
        print json.dumps(data)
        self.s.post(self.address, data={'access_token': self.access_token, 'params': json.dumps(data)})


