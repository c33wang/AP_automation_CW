__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
import shlex, subprocess
import time




def max_throughput(mIPaddress):
    print "5G VHT20"
    controllerAP = AccessPoint(mIPaddress)
    controllerAP.configure_5g_channel_width(20)
    controllerAP.quit_browser()
    time.sleep(120)
    out = subprocess.check_output("iperf3 -f m -t 5 -O 3 -c 192.168.2.38", shell=True)
    outputlist = out.split('\n')
    print outputlist[len(outputlist)-5]
    print outputlist[len(outputlist)-4]

    print "5G VHT40"
    controllerAP = AccessPoint(mIPaddress)
    controllerAP.configure_5g_channel_width(40)
    controllerAP.quit_browser()
    time.sleep(120)
    out = subprocess.check_output("iperf3 -f m -t 5 -O 3 -c 192.168.2.38", shell=True)
    outputlist = out.split('\n')
    print outputlist[len(outputlist)-5]
    print outputlist[len(outputlist)-4]

    print "5G VHT80"
    controllerAP = AccessPoint(mIPaddress)
    controllerAP.configure_5g_channel_width(80)
    controllerAP.quit_browser()
    time.sleep(120)
    out = subprocess.check_output("iperf3 -f m -t 5 -O 3 -c 192.168.2.38", shell=True)
    outputlist = out.split('\n')
    print outputlist[len(outputlist)-5]
    print outputlist[len(outputlist)-4]

if __name__ == "__main__":
    max_throughput("192.168.1.250")

#ap = AccessPoint("mac-0418d6c0662f")
# ap.configure_5g_channel_width(20)
#
# apssh = MyAP('192.168.2.28')
# apssh.connect()
# ap.set_chainmask_5(1)



#ap = AccessPoint("192.168.1.17")
#ap.reboot_ap_stress(500)



