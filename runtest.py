__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *

ap = AccessPoint("mac-0418d6c0662f")
ap.configure_5g_channel_width(20)

apssh = MyAP('192.168.2.28')
apssh.connect()
ap.set_chainmask_5(1)