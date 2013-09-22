#!/usr/bin/python

# Echo server program
import socket
import json

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8888              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
	try:
		string = json.loads(data)
	except ValueError, e:
		break
	print "DECODED JSON: " + str(string)
        if not data: break
        print data
    conn.close()
