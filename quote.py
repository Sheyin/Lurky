# This module handles the !quote command and related functions
import json
import datetime
from datetime import date

# Called by !quote <quotation>, expects a string (quotation) and writes it to file.
def recordQuote(author, text):
	print("Passed to recordQuote: " + text)
	
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

	# Debug text to see if separation is working
	print("quoteRecord():")
	print("Original text: " + text)
	print("Author: " + author)
	print("Quoted author: " + quotedName)
	print("Quoted date: " + quotedDate)
	print("Quoted text: " + quotedText)
	print('\n')

	#json.JSONEncoder()

	# Prepare file for writing
	#filename = "quote.txt"
	#file = open(filename, "a")

	
	#file.write("Author: " + str(message.author) + " ID:" + str(message.author.id) + "\n")
	#file.write("Message: " + str(message.content) + "\n")
	#file.close()

	return


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
	print(dateCalculation("Yesterday at 4:50 PM"))
	print(dateCalculation("Last Friday at 5:50 PM"))
	print(dateCalculation("Last Wednesday at 5:50 PM"))