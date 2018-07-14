import requests
from bs4 import BeautifulSoup
import re


# Formats data for lurky
def getFortniteAlerts():
	results = getFortniteData()
	if results:
		response = "Important Alerts:\n"
		for alert in results:
			response += alert[0] + ': ' + alert[1] + ' ' + alert[2] + '\n'
	else:
		response = "Error retrieving data."
	return response

# Returns a list of tuples (item, level, missionType)
def getFortniteData():
	url = 'https://www.stormshield.one/'

	# query the website and return the html to the variable ‘page’
	page = requests.get(url)

	#print(page.text)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page.text, 'html.parser')

	# Take out the <div> of name and get its value
	alerts_box = soup.find('div', attrs={'class': 'hero__section--alerts'})

	# Separate tr's
	splitRows = str(alerts_box).split('</tr>')
	#print("Alerts Box:" + alerts_box.text + "\n")
	results = []

	for row in splitRows:
		regex = re.compile('row-legendary')
		#print('\n===Start=====\n')
		#print("row: " + str(row))
		#print('\n====End====\n')
		# This row has a legendary item
		if re.search(regex, str(row)):
			# Get the level of the mission
			tempSplit = row.split('<td class="')
			missionType = getMissionType(tempSplit[0])
			level = tempSplit[1][8:10]
			#print("tempSplit0:" + str(tempSplit[0]) + " tempSplit1: " + str(tempSplit[1]))
			#print("Level is:" + str(level) + ".")
			item = tempSplit[2][22:-7]
			if "vBucks" in item:
				truncated = item.split('\n')
				item = truncated[1]
			#print("Item is:" + str(item) + ".")
			results.append((item, level, missionType))
			#tempSplit2 = row.split('\\n')
			#print("tempSplit: " + str(tempSplit))
	return results


# Figure out the category (mission type) from a bit of string
def getMissionType(text):
	if 'repair' in text:
		return "Repair the Shelter"
	elif 'evacuate' in text:
		return "Evacuate the Shelter"
	elif 'bomb' in text:
		return "Deliver the Bomb"
	elif 'retrieve' in text:
		return "Retrieve the Data"
	elif 'fight' in text:
		return "Category 1 Storm / Fight the Storm"
	elif 'category-2' in text:
		return "Category 2 Storm"
	elif 'category-3' in text:
		return "Category 3 Storm"
	elif 'category-4' in text:
		return "Category 4 Storm"
	elif 'rocket' in text:
		return "Launch the Rocket"
	elif 'servers' in text:
		return "Protect the Servers"
	else:
		return "Unknown mission type"

# Prints the list of results
def printResults(results):
	print("Important Alerts: ")
	response = ""
	for alert in results:
		response += alert[0] + ': ' + alert[1] + ' ' + alert[2] + '\n'
	print(response)


# Pull all text from the BodyText div
#artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
#artist_name_list_items = artist_name_list.find_all('a')

if __name__ == "__main__":
	pass
	results = getFortniteData()
	printResults(results)
