import socket
import sys

s = socket.socket()
host = sys.argv[1]
port = sys.argv[2]
s.connect((host, int(port)))
print('connected to ' + host + ':' + str(port))
s.recv(1026)

