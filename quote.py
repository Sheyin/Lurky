# This module handles the !quote command and related functions
import json
import datetime
from datetime import date
import random
import users

filename = "quote.txt"
settingsFileName = "quoteSettings.txt"

# Called by !quote <quotation>, expects a string (quotation) and writes it to file.
def recordQuote(author, text):
	# Split text into appropriate parts
	# Format is like.. name - then a date string then \n and some quote
	# Using find here to locate the first instance only, since ' - ' may appear in the quoted text as well
	firstDash = text.find(' - ')
	quotedName = text[0:firstDash]

	# Separate date and quote from text
	splitContent = text[firstDash + 3:].splitlines()
	quotedDate = splitContent[0]

	# Tidy date into a standard format
	quotedDate = dateCalculation(quotedDate)

	# Get quotation
	quotedText = splitContent[1]

	# Identify correct quotedName if a nick was used
	quotedName = users.findUserID(quotedName)

	# Retrieve settings
	'''
	numQuotes = 0
	try:
		settingsFile = open(settingsFileName, "r")
		settingsJSON = settingsFile.read()
		settingsFile.close()
		settings = json.loads(settingsJSON)
		if not settings["numQuotes"]:
			settings["numQuotes"] = 0
		numQuotes = settings["numQuotes"]
	# No settings file, or blank settings file
	except (IOError, json.decoder.JSONDecodeError) as error:
		numQuotes = 0
	'''

	# Need another config file to count quote number, stats, etc
	#numQuotes += 1
	entry = {"date": quotedDate, "name": quotedName, "text": quotedText, "author": author}

	# Retrieve entire list of quotes to update the dictionary
	try:
		with open(filename, "r") as f:
			quotesDict = json.load(f)
		numQuotes = len(quotesDict)
		# Update dictionary
		quotesDict[str(numQuotes)] = entry
		# Write quote dictionary back to quotes.txt
		with open(filename, "w") as f:
			json.dump(quotesDict, f)
	# quotes filename does not exist or has no quotes
	except (IOError, json.decoder.JSONDecodeError) as error:
		# Reset quotesettings just to be on safe side
		numQuotes = 1
		# Write quote dictionary to quotes.txt
		newEntry = {numQuotes: {"date": quotedDate, "name": quotedName, "text": quotedText, "author": author}}
		
		with open(filename, "w") as f:
			json.dump(newEntry, f)

	# increment number of quotes in settings file
	settingsJSON2 = json.JSONEncoder().encode({"numQuotes": numQuotes})
	settingsFile = open(settingsFileName, "w")
	settingsFile.write(settingsJSON2 + "\n")
	settingsFile.close

	return

# Need a helper function to identify which quote, or else maybe default to a random?
def retrieveQuote(searchTerm, author):
	success = False
	# Check if searchTerm is null or contains some sort of parameter
	newTextArray = searchTerm.split(' ')
	if len(newTextArray) == 1:
		searchTerm = "random"
		success = True
	else:
		searchTerm = newTextArray[1].lower()
		if searchTerm == "me":
			searchTerm = author
		searchTerm = users.findUserID(searchTerm)
	
	# Retrieving quotes from filename
	# Deriving number of quotes from quotes dictionary
	try:
		with open(filename, "r") as f:
			quotesDict = json.load(f)
	except (IOError, json.decoder.JSONDecodeError) as error:
		# Empty or nonexistent settings file
		return "empty"

	if searchTerm != "random":
		searchResults = {}
		searchResultCount = 0
		for entry in quotesDict:
			if quotesDict[entry]["name"] == searchTerm:
				searchResultCount += 1
				searchResults[str(searchResultCount)] = quotesDict[entry]
		# Only turn search results into main dict if there were results for that entry
		if len(searchResults) > 0:
			quotesDict = searchResults
			success = True
		# No successful result found.
		else:
			success = False
	
	# Select a random quote from the selections
	quoteNumber = random.randint(1,len(quotesDict))
	quote = quotesDict[str(quoteNumber)]		

	# Getting non user-ID name to make it pretty?
	quote["name"] = users.findUserAlias(quote["name"])
	quote["author"] = users.findUserAlias(quote["author"])
	
	# Returns a dictionary of the specific quote with keys [date, name, text, author]
	return (quote, success)

# Discord automatically adds in "Yesterday" and "Today", "Last Tuesday", etc. which need to be converted to a date
# Older messages no longer have a timestamp (only date in MM/DD/YYYY format)
def dateCalculation(quotedDate):
	today = datetime.datetime.today()

	# Populate week calendar
	todayWeekday = str(today.strftime('%A'))
	weekDict = {}

	for i in range(1, 8):
		dayEntry = datetime.datetime.now() - datetime.timedelta(days=i)
		dayEntryLong = str(dayEntry.strftime('%A'))
		weekDict['Last ' + dayEntryLong] = str(dayEntry.strftime('%Y-%m-%d'))
	yesterdayEntry = datetime.datetime.now() - datetime.timedelta(days=1)
	weekDict['Yesterday'] = str(yesterdayEntry.strftime('%Y-%m-%d'))

	if "Today" in quotedDate:
		return str(today.strftime('%Y-%m-%d'))
	

	elif "Yesterday" in quotedDate:
		# Return day - 1
		return weekDict['Yesterday']

	# Automatically converts up to a week to "Last Tuesday", etc.
	elif "Last" in quotedDate:
		# Now locate entry in dictionary
		for key in weekDict:
			if key in quotedDate:
				return weekDict[key]

	else:
		print("Some error occurred.  Invalid date?  Returning today's date.")
		return str(today.strftime('%Y-%m-%d'))
			
	return

if __name__ == "__main__":
	#recordQuote("Me", "Lurky - Yesterday at 1:10PM\nThis is a test quote!")
	retrieveQuote()



