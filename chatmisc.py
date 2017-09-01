# Miscellaneous chat responses and functions
# Many of these messages are customized for my particular community and/or features from my earlier bots.

def quickMessageResponse(message, authorID):
	if greetingCheck(message):
		response = 'Hello <@' + authorID + '>! :grinning:'

	if partingCheck(message):
		response = "See 'ya, <@" + authorID + ">! :grinnning:"

	for _ in ["why lurky", "why are you named lurky", "who's lurky", "who is lurky"]:
		if _ in message:
			response = "I am a bot written in Python3 for the express purpose of entertaining some people and annoying the rest."

	if "fish" in message[:10]:
		response = '/me digs out the fish.'

	if "slap" in message[:10]:
		response =  'Meanie!'

	if "what is love" in message:
		response = "Baby don't hurt me... don't hurt me... no more..."

	for _ in ["give you up", "let you down", "run around", "desert you"]:
		if _ in message:
			response =  "Never gonna:\n```- give you up\n- let you down\n- run around\n- desert you\n```"

	return response

# Return a True or False if this a greeting to respond to.
def greetingCheck(message):
	# Check these for exact matches
	for _ in ['hi', 'hello', 'hiya', 'hiyas', 'hey', 'sup', 'helo', 'ola', 'hola', '/wave', 'morning', 'morn', 'evening', 'good evening']:
		if _ == message:
			return True
	# Then check for partial word matches
	for _ in ['hi ', 'hello ', 'hey ']:
		if greeting in message.content[:5]:
			return True
	return False

# Return True or False if this is a greeting to respond to.
def partingCheck(message):
	for _ in ["bye", "see 'ya", "later", "ja", "nn", "night", "g'night", "g'nite", "nite", "ja ne", "laters"]:
		if _ == message		
			return True
	return False

