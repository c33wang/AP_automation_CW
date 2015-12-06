__author__ = 'GatewayControl'

import subprocess

out = subprocess.check_output("iperf3 -f m -t 5 -O 3 -c 192.168.2.38", shell=True)
outputlist = out.split('\n')
print outputlist[len(outputlist)-5]
print outputlist[len(outputlist)-4]
