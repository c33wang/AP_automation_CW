import paramiko
import time
import re


class MyAP:

    def __init__(self, ip):

        self.ip = ip
        self.username = "root"
        self.password = "admin"

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(self.ip, username = self.username, password = self.password)

    def close(self):
        self.ssh.close()

    def get_countrycode(self):
        stdin, stdout, stderr = self.ssh.exec_command('cat /tmp/system.cfg | grep radio.countrycode')
        tmp_list = stdout.read().split('=')
        print tmp_list[1]
        return int(tmp_list[1])

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        for line in stdout.read().splitlines():
            print line

    def get_ver(self):
        stdin, stdout, stderr = self.ssh.exec_command('mca-cli-op info')
        infostr = stdout.read()
        return re.search('Version:\s*(.+)\s*', infostr).group(1)

    def set_chainmask_2(self, bitmask):
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 txchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 rxchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi0 down')
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi0 up')
        time.sleep(1)
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_txchainmask')
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_rxchainmask')

    def set_chainmask_5(self, bitmask):
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 txchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 rxchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi1 down')
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi1 up')
        time.sleep(1)
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 get_txchainmask')
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 get_rxchainmask')


    def set_bw_5(self, bw):
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv ath2 mode 11ACVHT' + str(bw))
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig ath2 down')
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig ath2 up')

    def set_bw_2(self, bw):
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv ath0 mode 11NGHT' + str(bw))
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig ath0 down')
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig ath0 up')



#########################################openwrt#################################################

    def wrt_restart(self):
        stdin, stdout, stderr = self.ssh.exec_command('/etc/init.d/network restart')

    def wrt_set_bw_5(self, bw):
        stdin, stdout, stderr = self.ssh.exec_command('uci set wireless.wifi1.htmode=HT' + str(bw))

    def wrt_set_ch_5(self, ch):
        stdin, stdout, stderr = self.ssh.exec_command('uci set wireless.wifi1.channel=' + str(ch))

    def wrt_set_bw_2(self, bw):
        stdin, stdout, stderr = self.ssh.exec_command('uci set wireless.wifi0.htmode=HT' + str(bw))

    def wrt_set_bw_2(self, ch):
        stdin, stdout, stderr = self.ssh.exec_command('uci set wireless.wifi0.channel=' + str(ch))



def get_station_info(ssh_ap_address):
    sshap = MyAP(ssh_ap_address)
    sshap.connect()

    sshap.wrt_set_ch_5(ch)
    sshap.wrt_restart()




    sshap.close()

if __name__ == "__main__":
    get_station_info('192.168.1.1')








    # fo = open('commands', 'r')
    # for line in fo:
    #     command = line
    #     ap.exec_command(command)
    #     time.sleep(1)









##ssh = paramiko.SSHClient()
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##ssh.connect("192.168.1.218", username='admin', password = 'admin')
##
##stdin, stdout, stderr = ssh.exec_command('iwconfig')
##output = stdout.readlines()
##
##print output
