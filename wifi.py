__author__ = 'GatewayControl'
import subprocess
import time



def ping_test(sourceIp='10.1.7.31', wlan_network="10"):
    subprocess.call("netsh wlan disconnect")
    time.sleep(5)
    #subprocess.call("netsh wlan connect name=\"jerry-corp-2g\"")
    subprocess.call("netsh wlan connect name=" + wlan_network)
    time.sleep(2)
    #ping from source address 10.1.7.31
    subprocess.call("ping 8.8.8.8 -S " + sourceIp)
    time.sleep(5)

if __name__ == "__main__":
    ping_test('192.168.1.238', '10')
