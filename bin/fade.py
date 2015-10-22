import time
from random import randint
from ConfigParser import SafeConfigParser

from iot_controller.ledAsAService import TricolorLED

parser = SafeConfigParser()
parser.read('config.ini')

myLED = TricolorLED(
    address=parser.get('device', 'address'),
    access_token=parser.get('device', 'access_token'),
)

rLast = 0
gLast = 0
bLast = 0

while 1:
    rNew = randint(0, 255)
    gNew = randint(0, 255)
    bNew = randint(0, 255)

    res = 100.0

    for step in range(int(res)):
        myLED.rgb(rLast + (rNew-rLast)*(step/res),
                     gLast + (gNew-gLast)*(step/res),
                     bLast + (bNew-bLast)*(step/res))
        time.sleep(0.01)

    rLast = rNew
    gLast = gNew
    bLast = bNew


