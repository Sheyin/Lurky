# Miscellaneous chat responses and functions
# Many of these messages are customized for my particular community and/or features from my earlier bots.

def quickMessageResponse(message, authorID):
	if greetingCheck(message):
		response = 'Hello <@' + authorID + '>! :grinning:'

	if partingCheck(message):
		response = "See 'ya, <@" + authorID + ">! :grinnning:"

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
	for greeting in ['hi', 'hello', 'hey', 'sup', 'helo', 'ola', "/wave", "morni", "eveni"]:
			if greeting in message.content[:5]:
				return True
	return False

# Return True or False if this is a greeting to respond to.
def partingCheck(message):
	for greeting in ["bye", "see 'ya", "later", "ja", "nn", "night", "g'night", "g'nite", "nite"]
	return False

