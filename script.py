#!/usr/bin/python3

from ipaddress import ip_address


initial_ips = open('initial_ips.txt', 'r')
ips = open('ips.txt', 'w')

for addr in initial_ips:
	try:
		a = ip_address(addr)
		if not a.is_private:
			ips.write(addr)

	except ValueError:
		pass
initial_ips.close()
ips.close()
