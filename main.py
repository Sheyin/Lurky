# An experimental Discord Bot
# Don't get your hopes up.  It will probably suck.

import socket
import secret

# imaginary values
TCP_IP = '127.0.0.1'
TCP_PORT = 5760
BUFFER_SIZE = 1024
MESSAGE = "Test!"

# If use a token, need something like:
# Authorization: TOKEN_TYPE TOKEN in the http header
# User-Agent: DiscordBot ($url, $versionNumber)

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send = s.recv(BUFFER_SIZE)
s.close()

print "Received data: ", data



# References:
# https://pythonspot.com/en/python-network-sockets-programming-tutorial/