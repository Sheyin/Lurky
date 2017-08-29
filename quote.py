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
	print("Today's date: " + str(today.strftime('%Y-%m-%d')))
	year = month = today.strftime('%Y')
	month = today.strftime('%B')
	day = today.strftime('%d')
	print("Month: " + month + " Day: " + day + " Year: " + year)
	print("Yesterday: " + month + " " + int(day)-1 + " " + year)

	if "Yesterday" in quotedDate:
		# Return day - 1
		pass

	# Automatically converts up to a week to "Last Tuesday", etc.
	elif "Last" in quotedDate:
		# Figure out today's day then calculate how long ago it was
		week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		for index, weekday in enumerate(week, start = 0):
			if weekday in quotedDate:
				weekIndex = index
		print("weekIndex: " + weekIndex + " day: " + week[weekIndex])

	
	return