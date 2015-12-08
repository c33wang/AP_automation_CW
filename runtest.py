__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
import subprocess
import time


iperf3_command = "iperf3 -f m -t 5 -O 3 -c 192.168.2.38"




def max_throughput(mIPaddress):
    print "5G VHT20"
    controllerAP = AccessPoint(mIPaddress)
    controllerAP.configure_5g_channel_width(20)
    controllerAP.quit_browser()
    time.sleep(120)
    out = subprocess.check_output(iperf3_command, shell=True)
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

def chainmask_throughput(cIPaddress):
    sshap = MyAP(cIPaddress)
    sshap.connect()

    sshap.set_chainmask_5(1)
    sshap.exec_command('iwpriv wifi1 get_txchainmask')

    sshap.set_chainmask_5(2)
    sshap.exec_command('iwpriv wifi1 get_txchainmask')


    sshap.set_chainmask_5(4)
    sshap.exec_command('iwpriv wifi1 get_txchainmask')


    #max_throughput(cIPaddress)





if __name__ == "__main__":
    #max_throughput("192.168.1.250")
    #chainmask_throughput("192.168.1.250")

    #print "5G VHT20"
    #controllerAP = AccessPoint(mIPaddress)
    #controllerAP.configure_5g_channel_width(20)
    #controllerAP.quit_browser()
    #time.sleep(120)
    out = subprocess.check_output(iperf3_command, shell=True)
    outputlist = out.split('\n')
    print outputlist[len(outputlist)-5]
    print outputlist[len(outputlist)-4]






