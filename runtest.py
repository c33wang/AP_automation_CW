__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
import subprocess
import time


iperf3_command = "iperf3 -f m -t 50 -O 3 -c 192.168.2.38"
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
        time.sleep(90)

        for bitmaskk in [1, 2, 4]:
            sshap.set_chainmask_5(bitmaskk)
            sshap.exec_command('iwpriv wifi1 get_txchainmask')
            time.sleep(95)
            out = subprocess.check_output(iperf3_command, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]




def max_throughput_2(mIPaddress):

    sshap = MyAP(mIPaddress)
    sshap.connect()

    for x in [20]:
        print "2G HT%d" %x
        controllerAP = AccessPoint(mIPaddress)
        controllerAP.configure_2g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(90)

        for bitmaskk in [1, 2, 4, 7]:
            sshap.set_chainmask_2(bitmaskk)
            sshap.exec_command('iwpriv wifi0 get_txchainmask')
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
    max_throughput_2(mIPaddress)

    #print "5G VHT20"
    #controllerAP = AccessPoint(mIPaddress)
    #controllerAP.configure_5g_channel_width(20)
    #controllerAP.quit_browser()
    #time.sleep(120)
    # out = subprocess.check_output(iperf3_command, shell=True)
    # outputlist = out.split('\n')
    # print outputlist[len(outputlist)-5]
    # print outputlist[len(outputlist)-4]







