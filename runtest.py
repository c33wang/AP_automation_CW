__author__ = 'GatewayControl'

from controller import *
from ap_ssh import *
from wifi import *
import os
import shlex, subprocess


#subprocess.Popen(subprocess.Popen(r'', cwd=r'C:\Program Files (x86)\Ixia\IxChariot'))

# os.chdir("C:\Program Files (x86)\Ixia\IxChariot")
# subprocess.call("cd C:\Program Files (x86)\Ixia\IxChariot")
# subprocess.call("dir")




# ap = AccessPoint("mac-0418d6c0662f")
# ap.configure_5g_channel_width(20)
#
# apssh = MyAP('192.168.2.28')
# apssh.connect()
# ap.set_chainmask_5(1)



# command_line = raw_input()
# args = shlex.split(command_line)
# print args
# subprocess.Popen(args)

#path = shlex.split('C:\Program Files (x86)\Ixia\IxChariot')
#command = shlex.split('runtst.exe C:\ChariotAuto\Interop\5G\TestCase\Throughput.tst')

#subprocess.Popen(command, cwd=path)


out = subprocess.check_output("iperf3 -f m -t 5 -O 3 -c 192.168.2.38", shell=True)
outputlist = out.split('\n')
print outputlist[len(outputlist)-5]
print outputlist[len(outputlist)-4]


