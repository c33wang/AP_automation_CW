##JFW model 50PA-520
##Telnet into attenuators

import telnetlib
import time

def set_attntn(value):
    #value = attenuation ranges from 0 to 95
    tn = telnetlib.Telnet("192.168.2.34", "3001")
    tn.write("saa " + str(value) + " \n")
    time.sleep(1)
    print tn.read_very_eager()
    tn.write("exit\n")

if __name__ == "__main__":
    set_attntn(56)
