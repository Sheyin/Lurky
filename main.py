# An experimental Discord Bot
# Don't get your hopes up.  It will probably suck.

import socket
import secret

# imaginary values
HOST = '127.0.0.1'
PORT = 32457
apiSource = "https://discordapp.com/api"
# # bytes received at a time from the server
BUFFER_SIZE = 1024
MESSAGE = "Test!"
secret = secret.botToken

# Important URL's
# OAuth2 Base authorization URL
authorizeURL = "https://discordapp.com/api/oauth2/authorize"
# OAuth2 Token URL
tokenURL = "https://discordapp.com/api/oauth2/token"
# OAuth2 Revocation URL
revokeURL = "https://discordapp.com/api/oauth2/token/revoke"


# If use a token, need something like:
# Authorization: TOKEN_TYPE TOKEN in the http header
# User-Agent: DiscordBot ($url, $versionNumber)


s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# Sends the string as bytes
s.send(b'Test!')
data = s.recv(BUFFER_SIZE)
s.close()

print "Received data: ", data


# Get gateway - cache and only retrieve if cached version fails
def getGateway ():
	# expected response format:
	# {
	#	"url": "wss://gateway.discord.gg/"
	# }

# Heartbeat - op1 should be sent every x milliseconds
heartbeat = '{"op": 1,"d": 251}'

# References:
# https://pythonspot.com/en/python-network-sockets-programming-tutorial/