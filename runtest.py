__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
import subprocess
import time


iperf3_command = "iperf3 -f m -t 5 -O 3 -c 192.168.1.232"
mIPaddress = "192.168.2.24"




def max_throughput(mIPaddress):
    for x in [20, 40, 80]:
        print "5G VHT%d" %x
        controllerAP = AccessPoint(mIPaddress)
        controllerAP.configure_5g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(120)
        out = subprocess.check_output(iperf3_command, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]


def chainmask_throughput(mIPaddress):

    sshap = MyAP(mIPaddress)
    sshap.connect()

    for x in [20, 40, 80]:
        print "5G VHT%d" %x
        controllerAP = AccessPoint(mIPaddress)
        controllerAP.configure_5g_channel_width(x)
        controllerAP.quit_browser()

        for bitmaskk in [1, 2, 4]:
            time.sleep(90)
            sshap.set_chainmask_5(bitmaskk)
            sshap.exec_command('iwpriv wifi1 get_txchainmask')
            time.sleep(95)
            out = subprocess.check_output(iperf3_command, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]




    # sshap.set_chainmask_5(1)
    # sshap.exec_command('iwpriv wifi1 get_txchainmask')
    #
    # sshap.set_chainmask_5(2)
    # sshap.exec_command('iwpriv wifi1 get_txchainmask')
    #
    # sshap.set_chainmask_5(4)
    # sshap.exec_command('iwpriv wifi1 get_txchainmask')
    # max_throughput(mIPaddress)




if __name__ == "__main__":
    #max_throughput("192.168.1.250")
    chainmask_throughput(mIPaddress)

    #print "5G VHT20"
    #controllerAP = AccessPoint(mIPaddress)
    #controllerAP.configure_5g_channel_width(20)
    #controllerAP.quit_browser()
    #time.sleep(120)
    # out = subprocess.check_output(iperf3_command, shell=True)
    # outputlist = out.split('\n')
    # print outputlist[len(outputlist)-5]
    # print outputlist[len(outputlist)-4]







