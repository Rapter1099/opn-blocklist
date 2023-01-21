#!/usr/bin/python3

from ipaddress import ip_address

with open('initial_ips.txt') as initial_ips:
	lines = [line.rstrip() for line in initial_ips]
	ips = open('ips.txt', 'w')
	for addr in lines:
		try:
			a = ip_address(addr)
			if not a.is_private:
				ips.write(addr+"\n")
		except ValueError:
			print("ValueError")
initial_ips.close()
ips.close()
