repeat

	try
		do shell script "ping -c 1 192.168.1.1"
	on error

		do shell script "networksetup -setairportpower en0 off"
		do shell script "networksetup -setairportpower en0 on"
	end try

	delay 90



end repeat