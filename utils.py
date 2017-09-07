# Misc functions

import json
import secret
import users

statsList = ["!fish", "!slap", "!test", "!quote", "!getquote", "!fish_target", "!slap_target", "!quote_target"]
statsfile = "stats.txt"	# note that this is doubly declared in chatsmisc.py - should standardize into a single variable

''' Sample valid json:
{
	"Sheyin#1234": {
		"!fish": 0,
		"!slap": 0,
		"!test": 0,
		"!quote": 0,
		"!getquote": 0,
		"!fish_target": 0,
		"!slap_target": 0,
		"!quote_target": 0
	}
}
'''

# Keeping track of random command usage statistics.
# A file check should be performed when Lurky starts, so this should generally succeed.
def updateStats(stat, userID):
	try:
		with open(statsfile, "r") as f:
			statsDict = json.load(f)
		# find stat in question and get value
			statValue = statsDict[userID][stat]
			statValue += 1
		# Update dictionary
		statsDict[userID][stat] = statValue
		# Write stats dictionary back to statsfile
		with open(statsfile, "w") as f:
			json.dump(statsDict, f)

	# Stats file does not exist or the dictionary is missing that entry
	except (IOError, json.decoder.JSONDecodeError) as error:
		print("Error: unable to update " + stat + ".  Restart Lurky.")



# Checks if the stats dictionary exists and has all the requested variables.
# May want to store the list elsewhere.
def checkInitialization():
	try:
		with open(statsfile, "r") as f:
			statsDict = json.load(f)
		# Check and make sure all the stats have an entry
			for user in statsDict:
				for _ in statsList:
					if _ not in statsDict[user]:
						print("Error: unable to find " + _ + " for user " + user)

	# Stats file does not exist or something is broken - reset stats file completely
	except (IOError, json.decoder.JSONDecodeError) as error:
		statsDict = {}
		for userID in secret.usernameList:
			newEntry = {"!fish": 0, "!slap": 0, "!test": 0, "!quote": 0, "!getquote": 0, "!fish_target": 0, "!slap_target": 0, "!quote_target": 0}
			statsDict[userID] = newEntry
		with open(statsfile, "w") as f:
			json.dump(statsDict, f)
	return


# Experiment to see if stats file is correct
def retrieveAllStats():
	try:
		with open(statsfile, "r") as f:
			statsDict = json.load(f)
			return statsDict

	# Stats file does not exist or the dictionary is missing that entry
	except (IOError, json.decoder.JSONDecodeError) as error:
		print("Error: unable to update " + stat + ".  Restart Lurky.")


# Retrieve a specific set of stats - is this necessary?
def retrieveStats(statParameter, targetParameter):
	allData = retrieveAllStats()
	if statParameter == "all":
		return allData[targetParameter]
	else:
		return allData[targetParameter][statParameter]


# Returns the requested stat
def getStats(message, author):
	# Get content after !stats command
	splitMessage = message.split(' ')
	if len(splitMessage) == 1:
		return "Which stat would you like information about?\nUsage: !stat nameOfStat person(optional)\nStats: !fish, !slap, !test, !quote!, !getquote, !fish_target, !slap_target, !quote_target"
	else:
		# Figure out which parameter was provided
		# use userID to see if there is a recognized user
		user = users.findUserID(splitMessage[1])
		if not user:
			stat = checkIfStat(splitMessage[1])
			
			if not stat:
				print("Error: undefined stat")
				return 'Unrecognized parameter "' + splitMessage[1] + '".'
			else:
				targetParameter = author
				statParameter = stat
				#print("statParameter: " + statParameter + " targetParameter: " + targetParameter)
		else:
			targetParameter = user
			statParameter = "all"
	# Assuming len = 3 though
	if len(splitMessage) > 2:
		# use userID to see if there is a recognized user
		user = splitMessage[2]
		if not user:
			stat = checkIfStat(splitMessage[2])
			# Parameter 2 is unrecognized, can operate only using parameter 1 instead
			if not stat:
				print('Unrecognized parameter "' + splitMessage[2] + '".')
			# Parameter 2 is a stat, user should already be defined at this point
			else:
				statParameter = stat
		# Parameter 2 is a user, stat should already be defined at this point
		else:
			# Check if user is really a known user
			tempUser = users.findUserID(user)
			if tempUser:
				targetParameter = tempUser
			# Unrecognized second parameter (user)
			else:
				print("Error: unrecognized second parameter (user)")
				targetParameter = author

	requestedData = retrieveAllStats()

	response = "Here is the requested data: " + statParameter + " stats for " + targetParameter + ".\n"
	if statParameter != "all":
		# times vs time
		if requestedData[targetParameter][statParameter] == 1:
			response += targetParameter + " has used " + statParameter + " " + str(requestedData[targetParameter][statParameter]) + " time."
		response += targetParameter + " has used " + statParameter + " " + str(requestedData[targetParameter][statParameter]) + " times."
	else:
		response += "```"
		addition = ""
		for _ in statsList:
			data = requestedData[targetParameter][_]
			addition = _ + ": " + str(data) + " times.\n"
			response += addition
		response += "```"
	return response

def checkIfStat(text):
	#print("checkIfStat: " + text)
	for _ in statsList:
		if _ == text:
			#print("Stat found!")
			return _
	print("Error in checkIfStat: no matching stat found.")


if __name__ == "__main__":

	pass