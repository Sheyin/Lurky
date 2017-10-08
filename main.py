# Adapted from discord.py documentation example.

import discord
import asyncio
import secret
import users
import quote
import chatmisc
import datetime
import utils

client = discord.Client()
# This checks for and creates a stats file if it does not exist
utils.checkInitialization()

# Needed for voice
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

#async def create_voice_client(self, channel):
 	#

@client.event
async def on_ready():
    print(str(client.user.name) + ' here, reporting for duty!')
    print('------')

@client.event
async def on_message(message):
	# Check contents of message
	if users.findUserAlias(str(message.author)) == "teague" and "lurkey" in str(message.content).lower():
		response = teague.chat(message.content)
		await client.send_message(message.channel, response)
	if message.content.startswith('!quote '):
		quote.recordQuote(str(message.author), str(message.content)[7:])
		utils.updateStats("!quote", str(message.author))
		await client.send_message(message.channel, 'Quote has been recorded.')
	if message.content.startswith('!getquote'):		
		quoteDict, success = quote.retrieveQuote(str(message.content), str(message.author))
		utils.updateStats("!getquote", str(message.author))
		if quoteDict == "empty":
			await client.send_message(message.channel, 'Sorry, there are no quotes recorded.  Add some now using !getquote (userID/date/quote as copy-pasted from Discord)!')
		elif not success:
			await client.send_message(message.channel, 'No quotes by that name found.  Here is a random quote: "' + quoteDict['text'] + ' -- ' + quoteDict['name'] + ', (quoted by ' + quoteDict['author'] + '), ' + quoteDict['date'])
		else:
			await client.send_message(message.channel, 'Quote: "' + quoteDict['text'] + ' -- ' + quoteDict['name'] + ', (quoted by ' + quoteDict['author'] + '), ' + quoteDict['date'])

	if message.content.startswith('!test') or message.content.startswith('test'):
		utils.updateStats("!test", str(message.author))
		response = chatmisc.test(message.author)
		await client.send_message(message.channel, response)

	if message.content.startswith('!tryid'):
		await client.send_message(message.channel, 'Testing <@' + str(message.author.id) + '>')

	if message.content.startswith('!slap'):
		response = chatmisc.slap(message.content.lower(), str(message.author))
		utils.updateStats("!slap", str(message.author))
		await client.send_message(message.channel, response)

	if message.content.startswith('!fish'):
		response = chatmisc.fish(message.content.lower(), str(message.author))
		utils.updateStats("!fish", str(message.author))
		await client.send_message(message.channel, response)

	if message.content.startswith('!stats'):
		response = utils.getStats(message.content.lower(), str(message.author))
		await client.send_message(message.channel, response)

	if message.content.startswith('!help'):
		response = chatmisc.help(message.content.lower())
		await client.send_message(message.channel, response)

	if message.content.startswith('Lurky?'):
		await client.send_message(message.channel, 'Yes?')
		
	# So it doesn't respond to itself
	elif message.author.id != message.server.me.id:
		# Logging just because
		try:
			with open("log.txt", "a") as file:
				file.write("Author: " + str(message.author) + " ID:" + str(message.author.id) + " Date: " + datetime.datetime.today().strftime("%d/%m/%y %H:%M") + "\n")
				file.write("Message: " + str(message.content) + "\n")
		except UnicodeEncodeError:
			with open("log.txt", "a") as file:
				file.write("Author: " + str(message.author) + " ID:" + str(message.author.id) + " Date: " + datetime.datetime.today().strftime("%d/%m/%y %H:%M") + "\n")
				file.write("Message: " + "Some emote was used that produces a unicode error." + "\n")
	
		if "surprise" in message.content.lower():
			if message.author.voice_channel:
				if not client.is_voice_connected(message.server):
					voice = await client.join_voice_channel(message.author.voice_channel)
					player = voice.create_ffmpeg_player('sound/GiveYouUpIntro.mp3')
					player.start()
					print("Here's a surprise for " + str(message.author)[:-5] + "!")
				else:
					voice = await client.is_voice_connected(message.author.voice_channel)
					player = voice.create_ffmpeg_player('sound/GiveYouUpIntro.mp3')
					player.start()
				#else:
					print("I might be in the wrong channel.")
					print(str(message.author)[:-5] + " is in " + str(message.author.voice_channel) + " and server " + str(message.server) + ".")
					#await client.move_to(message.author.voice_channel)
				#try:
				#player = voice.create_ffmpeg_player('sound/GiveYouUpIntro.mp3')
				#player.start()
				#print("Here's a surprise for " + str(message.author)[:-5] + "!")
				'''except:
					print("Something failed during voice test.")
					print("Is Opus loaded?: " + str(discord.opus.is_loaded()))
					# Need a custom error handler if you want to display the error
					pass
					'''
			else:
				await client.send_message(message.channel, 'I only give surprises to people in voice chat!')

		# This seems to throw errors on a regular basis.  Returns "video does not exist"
		elif message.content.startswith('!play '):
			# Parse url first and see if it is valid
			splitString = message.content.lower().split(' ')
			if len(splitString) == 1:
				await client.send_message(message.channel, 'What do you want to play?  Enter "!play youtube-url-here"')
			else:
				if splitString[1][0:4] == 'http':
					url = splitString[1]
					if message.author.voice_channel:
						try:
							# Probably want to add a case for "if already joined voice channel" or else throws error
							voice = await client.join_voice_channel(message.author.voice_channel)
							# Test - from https://github.com/Rapptz/discord.py/issues/315
							beforeArgs = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
							#player = await voice.create_ytdl_player(url)
							player = await voice.create_ytdl_player(url, ytdl_options="--ignore-errors", before_options=beforeArgs)
							player.start()
							print("Successful?")

						except:
							print("Something failed during voice test")
							print("Is Opus loaded?: " + str(discord.opus.is_loaded()))
							print("Url tried to play: " + url)
							pass

					else:
						await client.send_message(message.channel, 'No surprise for you!')
				else:
					await client.send_message(message.channel, "Error: " + str(splitString[1]) + " is not a valid youtube url.")

		response = chatmisc.quickMessageResponse(message.content.lower(), message.author)
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