# Lurky
Experimental discord bot in Python (3.6).  Created to mimic my old irc bot/scripts and mostly customized to work around my community.

## Requires:
1. <a href="https://github.com/Rapptz/discord.py">discord.py</a> 
 - install with <b>pip install discord.py</b>  
 - Note that as of 8/31/17 there may be an error running this on macOS.
2. secret.py (a config file - need to create something to auto-populate this)
 - This contains private info such as the token required by discord.
 - generate a python module with "token = (your token from discord)".
 - Also contains usernameList dictionary for personal use - this associates aliases with Discord usernames.
3. A folder named /sound/ and a specific mp3 file inside.  Used only with the "surprise" command.  File not uploaded to repo for fear of copyright infringement.

## Usage:
<b>Python main.py</b> or if there are multiple python installations, <b>Python3 main.py</b>.

## Features:
### Greets people automatically or responds to parting messages
- This has been customized respond to my particular community's greetings. ("hello", "hi", "nn", "bye", etc)
- Lurky will look at the time, and give a time-appropriate response to the greeting/parting message.  Sometimes he even uses emotes.
### Responds to a several !commands:
- __!help__ (optional parameter: specific command): Summarizes the available commands.  If a specific command is given, ex. "!help !quote", it will give more detailed information on that command and provide usage information.
- __!slap__: Causes Lurky to slap a target (in text).
- __!fish__: A variation of the !slap command, ported from my original IRC script.
- __!test__: Just tells you "working" if Lurky heard your command - ex. if you are wondering if you lost connection.
- __!quote__: Records a quote.  Expected input is the copy-pasted input from Discord (including name of speaker, time, and quoted text).
  - Quotes are stored locally in JSON format in a text file (quote.txt).  
  - If it does not exist, it will be created automatically.
- __!getquote__ (optional parameter: name): Retrieves a random quote.  If a name (alias or discord ID) of a person is provided, Lurky will try to retrieve a quote from that person, or else it will pull a random one.
  - It will default to referring to a "preferred alias" (first alias listed in secret.usernameList) when referring to the person quoted.  If a quoted person does not have an entry in the usernameList, it will simply refer to that person by their Discord ID.
- __!stats__ (optional parameters: name, stat): Retrieves command usage statistics (for a specific user and/or command, if provided).
  - Lurky automatically records stats on how often certain commands are used, and by whom. 
  - It should not matter whether one parameter or both is provided, or what in order it is given.
  - These are stored locally in JSON format in a text file (stats.txt).  If it does not exist, or encounters an error, it should create a new one.
- __surprise__: A "hidden" command that only works if the user is in a voice channel.
- __!play__ (required parameter: link to video URL, ex. youtube): (buggy, but implemented) Plays a specified youtube video over user's voice channel.

## Known Issues:
- "surprise" only works once and may require a restart of Lurky to function again.
- "!play (link)" seems to have issues with certain links, stemming from youtube and youtube_dl, causing "video does not exist" errors.
- Some false positives on greetings/responses, fixed using better regular expressions, but there might be cases I overlooked.
- Disabled stats temporarily (logic with key errors found; need to investigate further)

