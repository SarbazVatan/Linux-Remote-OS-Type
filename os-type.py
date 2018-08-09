#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

def grab_os_type(ip):
	try:
		BOT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		BOT.connect((ip, 22))
		BOT.send('5353482d322e302d50755454595f52656c656173655f302e36390d0a')
		os_ = BOT.recv(1024)
		BOT.close()
		return os_.split(' ')[1]
	except:
		return None

if __name__ == '__main__':
	list_ = open(str(raw_input("\n\n[*]Servers: ")), 'r').readlines()
	for xx in list_:
		os_type = grab_os_type(xx.strip())
		if os_type != None:
			string_ = "{}|{}".format(xx.strip(), os_type)
		else:
			string_ = xx.strip()	
		with open("result.txt", 'a') as rs:
			rs.write(string_)
		rs.close()
		print string_
