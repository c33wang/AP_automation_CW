import paramiko
import time
import re


class MyAP:

    def __init__(self, ip):

        self.ip = ip
        self.username = "admin"
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
        # stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_txchainmask')
        # stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_rxchainmask')

    def set_chainmask_5(self, bitmask):
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 txchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi1 rxchainmask ' + str(bitmask))
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi1 down')
        stdin, stdout, stderr = self.ssh.exec_command('ifconfig wifi1 up')
        # stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_txchainmask')
        # stdin, stdout, stderr = self.ssh.exec_command('iwpriv wifi0 get_rxchainmask')






if __name__ == "__main__":
    ap = MyAP('192.168.2.24')
    ap.connect()
    ap.get_countrycode()
    ap.set_chainmask_5(4)


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
