__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
import subprocess
import time
from threading import Thread


#Screen Room Settling
iperf3_TX = "iperf3 -f m -t 30 -O 3 -c 192.168.1.174 -P 10"
iperf3_RX = "iperf3 -f m -t 30 -O 3 -c 192.168.1.174 -P 10 -R"
AP_iPaddress = "192.168.1.227"

# iperf3_TX = "iperf3 -f m -t 6 -O 3 -c 192.168.1.236 -P 10"
# iperf3_RX = "iperf3 -f m -t 6 -O 3 -c 192.168.1.236 -P 10 -R"
# AP_iPaddress = "192.168.2.24"


##############################################----5G----###############################################################
def max_throughput_5_ch(AP_iPaddress, iperf3_TX, iperf3_RX):
    for x in [20, 40, 80]:
        print "5G VHT%d TX:" %x
        controllerAP = AccessPoint(AP_iPaddress)
        controllerAP.configure_5g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(10)
        for ch in [36,40,44,48,149,153,157,161]:
            controllerAP = AccessPoint(AP_iPaddress)
            controllerAP.configure_5g_channel(ch)
            controllerAP.quit_browser()
            print "Channel:" + str(ch)
            time.sleep(180)
            out = subprocess.check_output(iperf3_TX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]

            print "5G VHT%d RX:" %x
            out = subprocess.check_output(iperf3_RX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]


def max_throughput_5(AP_iPaddress):
    for x in [20, 40, 80]:
        print "5G VHT%d TX:" %x
        controllerAP = AccessPoint(AP_iPaddress)
        controllerAP.configure_5g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(120)
        out = subprocess.check_output(iperf3_TX, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]

        print "5G VHT%d RX:" %x
        out = subprocess.check_output(iperf3_RX, shell=True)
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
            out = subprocess.check_output(iperf3_RX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]






def max_throughput_2(AP_iPaddress):
    for x in [20, 40]:
        print "2G VHT%d TX:" %x
        controllerAP = AccessPoint(AP_iPaddress)
        controllerAP.configure_2g_channel_width(x)
        controllerAP.quit_browser()
        time.sleep(120)
        out = subprocess.check_output(iperf3_TX, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]

        print "2G VHT%d RX:" %x
        out = subprocess.check_output(iperf3_RX, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]


def chainmask_throughput_2(mIPaddress):

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
            out = subprocess.check_output(iperf3_RX, shell=True)
            outputlist = out.split('\n')
            print outputlist[len(outputlist)-5]
            print outputlist[len(outputlist)-4]


def multithread():
        out = subprocess.check_output(iperf3_TX, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]
        print "5G VHT RX:"
        out = subprocess.check_output(iperf3_RX, shell=True)
        outputlist = out.split('\n')
        print outputlist[len(outputlist)-5]
        print outputlist[len(outputlist)-4]
        get_station_info('192.168.2.51')






def wrt_max_throughput_5_ch(ssh_ap_address):
    sshap = MyAP(ssh_ap_address)
    sshap.connect()

    for x in [20, 40, 80]:
        sshap.wrt_set_bw_5(20)
        for ch in [36,40,44,48,149,153,157,161]:
                sshap.wrt_set_ch_5(ch)
                sshap.wrt_restart()
                print "Channel:" + str(ch) + "      5G VHT%d TX:" %x
                time.sleep(30)
                out = subprocess.check_output(iperf3_TX, shell=True)
                outputlist = out.split('\n')
                print outputlist[len(outputlist)-5]
                print outputlist[len(outputlist)-4]
                time.sleep(10)
                print "Channel:" + str(ch) + "      5G VHT%d RX:" %x
                out = subprocess.check_output(iperf3_RX, shell=True)
                outputlist = out.split('\n')
                print outputlist[len(outputlist)-5]
                print outputlist[len(outputlist)-4]




if __name__ == "__main__":
    wrt_max_throughput_5_ch('192.168.1.1')
    # t1 = Thread(target=multithread())
    # t2 = Thread(target=get_station_info('192.168.2.51'))
    # t1.start()
    # t2.start()






    #max_throughput_2_ch(AP_iPaddress, iperf3_TX, iperf3_RX)

    #chainmask_throughput_2(AP_iPaddress)
    #max_throughput_2(AP_iPaddress)

    #print "5G VHT20"
    #controllerAP = AccessPoint(mIPaddress)
    #controllerAP.configure_5g_channel_width(20)
    #controllerAP.quit_browser()
    #time.sleep(120)
    # out = subprocess.check_output(iperf3_command, shell=True)
    # outputlist = out.split('\n')
    # print outputlist[len(outputlist)-5]
    # print outputlist[len(outputlist)-4]







