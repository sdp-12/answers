#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:11:15 2019
@author: stefania
"""

# Python program to implement client side of chat room. 
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ('Correct use: script name, IP address, port number')
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

while True: 

	# maintains a list of possible input streams 
	sockets_list = [sys.stdin, server] 

	""" There are two possible input situations. 
    1. server sends message to all connected client
    2. a client sends message to the server and all other connected client"""
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print (message) 
		else: 
			message = sys.stdin.readline() 
			server.send(message) 
#			sys.stdout.write("You:") 
#			sys.stdout.write(message) 
#			sys.stdout.flush() 
server.close() 
