# Does currency conversion, provided for at https://free.currencyconverterapi.com/
# Simple api / output: https://free.currencyconverterapi.com/api/v6/convert?q=USD_PHP&compact=y
# This only does 1 (first currency) into x amount of (second currency) so the calculation must be done here.

import requests
import json
import re
#from decimal import Decimal

# Gets currency conversion then formats a string to be returned.
def convertCurrency(amount, type):
	usdCurrency = getConversion(amount, type)
	amount = '{:,.2f}'.format(amount)
	response = amount + " JPY is equal to " + str(usdCurrency) + " USD."
	return response


# Converts currency and returns the amount in USD.
def getConversion(amount, type):
	# query the website and return the html to the variable ‘result’
	url = 'https://free.currencyconverterapi.com/api/v6/convert?q=USD_' + type + '&compact=y'
	responseResult = requests.get(url)
	formattedResult = json.loads(responseResult.text)
	result = formattedResult['USD_JPY']['val']

	# Divide the amount by the currency (formattedResult)
	tempResult = round(amount / result, 2)
	convertedResult = '${:,.2f}'.format(tempResult)
	# Round to cents (hundredth of a dollar)
	return convertedResult


# Only seeks out Japan's Yen (JPY) and sees if this is a conversion request.
def identifyCurrency(text):
	for jpnCurrency in ['jpn', 'jpy', 'yen', '¥', '円']:
		if jpnCurrency in text:
			# Strip all commas to be on the safe side
			text = text.replace(",","")
			regexCheck = ['\d+.?\d{1,2}\s' + jpnCurrency, jpnCurrency + '\s*\d+.?\d{1,2}']
			for _ in regexCheck:
				matchedRegex = re.search(_, text)
				if matchedRegex:
					matchedWord = matchedRegex.group()
					# Get currency in integer form
					amountString = ""
					for letter in matchedWord:
						if letter.isdigit() or letter == '.':
							amountString += letter
					amount = float(amountString)

					return amount


if __name__ == '__main__':
	amount = identifyCurrency("57,616.54 yen")
	response = convertCurrency(amount, 'JPY')
	print(response)

	# Aiming for: https://free.currencyconverterapi.com/api/v6/convert?q=15900JPY_USD&compact=y
	#getConversion(15900, 'JPY')

'''
	# Tests:
	print("15900yen:")
	amount = identifyCurrency("15900yen")
	print("Amount: " + str(amount))

	print("15900 yen:")
	amount = identifyCurrency("15900 yen")
	print("Amount: " + str(amount))

	print("yen 15900:")
	amount = identifyCurrency("yen 15900")
	print("Amount: " + str(amount))

	print("yen15900:")
	amount = identifyCurrency("yen 15900")
	print("Amount: " + str(amount))

	print("!convert 15900 yen:")
	amount = identifyCurrency("15900yen")
	print("Amount: " + str(amount))

	print("What is 15900 yen ???:")
	amount = identifyCurrency("15900 yen")
	print("Amount: " + str(amount))
'''
