# Miscellaneous chat responses and functions
# Many of these messages are customized for my particular community and/or features from my earlier bots.

import datetime
import random
import users
import utils

statsfile = "stats.txt"

def quickMessageResponse(message, author):
	response = ""
	authorID = str(author.id)
	if greetingCheck(message):
		response = createTimeResponse(True, authorID)

	if partingCheck(message):
		response = createTimeResponse(False, authorID)

	for _ in ["why lurky", "why are you named lurky", "who's lurky", "who is lurky"]:
		if _ in message:
			response = "I am a bot written in Python3 for the express purpose of entertaining some people and annoying the rest."

	if "what is love" in message:
		response = "Baby don't hurt me... don't hurt me... no more..."

	for _ in ["give you up", "let you down", "run around", "desert you"]:
		if _ in message:
			response =  "Never gonna:\n```- give you up\n- let you down\n- run around\n- desert you\n```"

	return response

# Return a True or False if this a greeting to respond to.
def greetingCheck(message):
	# Check these for exact matches
	for _ in ['hello', 'hiya', 'hiyas', 'helo', 'hola', '/wave', 'morni', 'even', 'good e', 'good m']:
		if _ in message[:6]:
			return True
	# Needs a stricter check than above
	for _ in ["hi", ":o", "ola", "sup", "hey"]:
		if _ in message[:3]:
			return True
	return False

# Return True or False if this is a greeting to respond to.
def partingCheck(message):
	for _ in ["bye", "see 'ya", "later", "night", "g'night", "g'nite", "nite", "laters"]:
		if _ in message[:7]:
			return True
	# Needs a stricter check than above
	for _ in ["nn", "ja", "gn"]:
		if _ in message[:2]:
			return True

	return False


# This checks if it is morning / afternoon / day for specific greetings.
def timeCheck():
	currentTime = datetime.datetime.today()
	if (currentTime.hour >= 6) and (currentTime.hour <= 12):
		return "morning"
	elif (currentTime.hour > 12) and (currentTime.hour < 18):
		return "afternoon"
	else:
		return "night"

# Called after a successful greetingCheck or partingCheck to provide a time-contextual response.
def createTimeResponse(isGreeting, authorID):
	time = timeCheck()
	# Percent chance of adding an emote on to the greeting or parting message.
	chanceForEmote = 50
	# List of possible messages and emotes to draw responses from
	dayPartingMessages = [
		"Have a good day <@" + authorID + ">!",
		"Have a great day <@" + authorID + ">!",
		"Have an awesome day, <@" + authorID + ">!",
		"Later, <@" + authorID + ">!",
		"Take care <@" + authorID + ">!",
		"See 'ya, <@" + authorID + ">!",
		]
	nightPartingMessages = [
		"Have a good night <@" + authorID + ">!",
		"Good night, <@" + authorID + ">!",
		"Night night <@" + authorID + ">!",
		"Sleep well, <@" + authorID + ">!",
		"Sweet dreams, <@" + authorID + ">!",
		"G'night <@" + authorID + ">!",
		]
	morningGreetingMessages = [
		"Morning, <@" + authorID + ">!",
		"Good morning, <@" + authorID + ">!",
		"Morning <@" + authorID + ">, hope you slept well!",
		"Hello there, <@" + authorID + ">!",
		"Hey <@" + authorID + ">!  Nice to see you!",
		]
	dayGreetingMessages = [
		"Hey there, <@" + authorID + ">!",
		"Hi <@" + authorID + ">!",
		"Hiyas <@" + authorID + ">!",
		"Well hello there, <@" + authorID + ">!",
		"Hey <@" + authorID + ">!  What's up?",
		]
	nightPartingEmotes = [
		":sleeping:",
		":zzz:",
		]
	greetingEmotes = [
		":grinning:",
		":grin:",
		":smiley_cat:",
		":wink:",
		":slight_smile:",
		]
	partingEmotes = [
		":v:",
		":ok_hand:",
		":thumbsup:",
		":vulcan:",
		]

	# Add on a emote to the message
	randomNumber = random.randrange(1, 101)
	if randomNumber <= chanceForEmote:
		useEmote = True
	else:
		useEmote = False 
	
	# Construct the actual message here.
	# Greeting message
	if isGreeting:
		if time == "morning":
			message = random.choice(morningGreetingMessages)
			if useEmote:
				message += " " + random.choice(nightPartingEmotes + greetingEmotes)
		else:
			message = random.choice(dayGreetingMessages)
			if useEmote:
				message += " " + random.choice(greetingEmotes)
	# Parting message
	else:
		if time == "night":
			message = random.choice(nightPartingMessages)
			if useEmote:
				message += " " + random.choice(nightpartingEmotes)
		else:
			message = random.choice(dayPartingMessages)
			if useEmote:
				message += " " + random.choice(partingEmotes)

	return message


# Implementation of chibi's old !fish command.  author will be used for tracking usage.

def fish(message, author):
	# Get content after !fish command
	splitText = message.split(' ')
	if len(splitText) > 1:
		appendThis = splitText[1]
	# No parameter (target) provided
	else:
		utils.updateStats("!fish_target", str(author))
		return "Uh, okay.  /me slaps <@" + str(author.id) + "> with one fish.\n/me slaps " + str(author)[:-5] + " with two fish.\n/me slaps " + str(author)[:-5] + " with a red fish.\n/me slaps " + str(author)[:-5] + " with a blue fish."

	# get userID
	userID, alias = users.findUserIDAndAlias(appendThis.lower())
	appendThisFragments = appendThis.split(alias)

	if users.findUserAlias(userID) in ["sheyin", "lurky"]:
		utils.updateStats("!fish_target", userID)
		message = "Meanie!"
	elif userID != "unknown":
		utils.updateStats("!fish_target", userID)
		message = "/me slaps " + userID[:-5] + " with one fish.\n/me slaps " + userID[:-5] + " with two fish.\n/me slaps " + userID[:-5] + " with a red fish.\n/me slaps " + userID[:-5] + " with a blue fish."
	# Unknown target - probably whatever is in appendThis, will be prone to errors.
	else:
		message = "/me slaps " + appendThis + " with one fish.\n/me slaps " + appendThis + " with two fish.\n/me slaps " + appendThis + " with a red fish.\n/me slaps " + appendThis + " with a blue fish."
	return message


# Implementation of chibi's old !slap command.  author will be used for tracking usage.
def slap(message, author):
	# Get content after !slap command
	splitText = message.split(' ')
	if len(splitText) > 1:
		appendThis = splitText[1]
	# No parameter (target) provided
	else:
		utils.updateStats("!fish_target", str(author))
		return "Uh, okay.  /me slaps <@" + str(author.id) + ">."
		# This does not work - it must be in format <@ numeric-id >
		#return "Uh, okay.  /me slaps @" + str(author)[:-5] + "."

	# get userID
	userID, alias = users.findUserIDAndAlias(appendThis.lower())
	appendThisFragments = appendThis.split(alias)

	if users.findUserAlias(userID) in ["Sheyin", "Lurky"]:
		utils.updateStats("!fish_target", userID)
		message = "Meanie!"
	elif users.findUserAlias(userID) == "Brandon":
		utils.updateStats("!fish_target", userID)
		message = "Meanie!\n/me slaps <@" + userID + ">"+ appendThisFragments[1] + "."
	elif userID != "unknown":
		utils.updateStats("!fish_target", userID)
		message = "/me slaps <@" + userID + ">"+ appendThisFragments[1] + "."
	# Unknown target - probably whatever is in appendThis, will be prone to errors.
	else:
		message = "/me slaps " + appendThis

	return message


# Print list of available commands in discord
def help(text):
	splitText = text.split(' ', 1)
	if len(splitText) == 1:
		return "The commands I have available are !quote, !getquote, !slap, !fish, !test, !stats.  You can use !help <command> to learn more.  I also have a few hidden features."
	elif splitText[1] == "!quote":
		return "Record a quote to be recalled later on.  Usage: !quote (copy-and-paste text from discord, including speaker and date, just as formatted by Discord itself)."
	elif splitText[1] == "!getquote":
		return "Bring up a random quote that was recorded by someone.  Usage: !getquote (optional parameter follows - ex. a name."
	elif splitText[1] == "!slap":
		return "Only mean people use this.  Use it to slap someone.  Usage: !slap (target name)."
	elif splitText[1] == "!fish":
		return "Slap someone around with a fish.  Usage: !slap (target name)."
	elif splitText[1] == "!test":
		return "Sometimes you just want to know if you've dc'ed or something.  Usage: !test (or just test)."
	elif splitText[1] == "!stats":
		return "Bring up stats about usage of various commands.  Usage: !stats (command) (user) for a specific stat, or just !stats (user) for all of that user's stats."
	else:
		return "Sorry, I don't know anything about " + splitText[1] + "!"



	
if __name__ == "__main__":
	pass
