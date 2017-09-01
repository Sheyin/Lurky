# Adapted from discord.py documentation example.

import discord
import asyncio
import secret
import users
import quote
from chatmisc import *
from datetime import date

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	# Check contents of message
	if message.content.startswith('!quote '):
		print ("Called quoteRecord()")
		quote.recordQuote(str(message.author), str(message.content)[7:])
		await client.send_message(message.channel, 'Quote has been recorded.')
	if message.content.startswith('!getquote'):		
		quoteDict, success = quote.retrieveQuote(str(message.content), str(message.author))
		if quoteDict == "empty":
			await client.send_message(message.channel, 'Sorry, there are no quotes recorded.  Add some now using !getquote (userID/date/quote as copy-pasted from Discord)!')
		elif not success:
			await client.send_message(message.channel, 'No quotes by that name found.  Here is a random quote: "' + quoteDict['text'] + ' -- ' + quoteDict['name'] + ', (quoted by ' + quoteDict['author'] + '), ' + quoteDict['date'])
		else:
			await client.send_message(message.channel, 'Quote: "' + quoteDict['text'] + ' -- ' + quoteDict['name'] + ', (quoted by ' + quoteDict['author'] + '), ' + quoteDict['date'])

	if message.content.startswith('!test'):
		await client.send_message(message.channel, 'Working!')

	if message.content.startswith('!tryid'):
		await client.send_message(message.channel, 'Testing <@' + str(message.author.id) + '>')

	if message.content.startswith('!slap'):
		# Get content after !slap command
		appendThis = str(message.content).split(' ', 1)[1]

		if "lurky" in appendThis.lower() or "sheyin" in appendThis.lower():
			await client.send_message(message.channel, "Meanie!")
		else:
			await client.send_message(message.channel, '/me slaps ' + appendThis + ".")

	if message.content.startswith('Lurky?'):
		await client.send_message(message.channel, 'Yes?')
		
	# So it doesn't respond to itself
	elif message.author.id != message.server.me.id:
		# Logging just because
		with open("log.txt", "a") as f:
			file.write("Author: " + str(message.author) + " ID:" + str(message.author.id) + " Date: " + datetime.datetime.today().strftime("%d/%m/%y %H:%M") + "\n")
			file.write("Message: " + str(message.content) + "\n")
	
		response = quickMessageResponse(message.content.lower(), str(message.author.id))
		if response:
			await client.send_message(message.channel, response)
		
	else:
		# Not needed - probably only something Lurky says.
		print("Lurky says: " + message.content)

# This line is necessary and should be at the very end of the script.
client.run(secret.token)

'''
	# From discord.py's documentation
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    '''