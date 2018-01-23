#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5008
BUFFER_SIZE = 1024
##MESSAGE = "Hello, World!"
NUMBER = "6"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(NUMBER)
data = s.recv(BUFFER_SIZE)
s.close()

print "Inputnumber:",NUMBER
print "received data:", data

