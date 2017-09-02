import secret

# This works with a dictionary of names maintained in secret.usernameList
# Expects this list to be a dict in format "DiscordID": ["array", "of", "names"]
# This is to match up common nicknames with a standard name (their proper user ID)
def findUserID(message):
	for ID in secret.usernameList:
		if ID in message.lower():
			return ID
		else:
			for alias in secret.usernameList[ID]:
				if alias in message.lower():
					return ID

# This works in reverse - given a user ID, it returns the first alias of that ID
def findUserAlias(userID):
	if userID not in secret.usernameList:
		print('Error: userID "' + userID + '" is not in the usernameList.')
		# may want to have it populate automatically or log if unknown user
		hashtagIndex = userID.find('#')
		alias = userID[0:hashtagIndex]
		return alias
	else:
		alias = secret.usernameList[userID][0].title()
		return alias

# This is similar to findUserID but it returns the ID as well as the alias used.
def findUserIDAndAlias(message):
	for ID in secret.usernameList:
		if ID in message.lower():
			return (ID, ID)
		else:
			for alias in secret.usernameList[ID]:
				if alias in message.lower():
					return (ID, alias)
	# Unknown user
	return ("unknown", "unknown")
	

if __name__ == "__main__":
	pass

