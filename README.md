# discordbot
Experimental discord bot in Python (3.6)

Requires:
<br><a href="https://github.com/Rapptz/discord.py">discord.py</a> - install with <b>pip install discord.py</b>  * Note that as of 8/31/17 there may be an error running this on mac.*
<br>secret.py (a config file - need to create something to auto-populate this)
- This contains private info such as the token required by discord.
- generate a python module with "token = (your token from discord)".
- Also contains usernameList dictionary for personal use - this associates aliases with Discord usernames.

Usage:
- <b>Python main.py</b> or if there are multiple python installations, <b>Python3 main.py</b>.

Known Issues:
- "surprise" only works once and may require a restart to function again.
- "!play (link)" seems to have issues with certain links, stemming from youtube and youtube_dl, causing "video does not exist" errors.
- Some false positives on greetings/responses, fixed many as they popped up but need more experimental data/observation.  May need to replace greetings with a regular expression for more strict responses.

