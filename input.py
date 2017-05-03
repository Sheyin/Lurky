import re

while input not in ['exit', 'quit']:
	input = raw_input(': ')
	if re.search('^A.+e', input):
		print "Found it!"