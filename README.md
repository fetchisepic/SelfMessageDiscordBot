# SelfMessageDiscordBot
|made by fetch, please give creds if ur gonna skid my code lmao|


# REQUIRMENTS
python 3.11.9 or higher
run `pip install -U discord.py` in your terminal

✅ Discord Developer Portal To-Do List
1. Create a New Application
Go to: https://discord.com/developers/applications

Click “New Application”

Give it a name and click “Create”

2. Create a Bot
Inside your application, click the “Bot” tab on the left

Click “Add Bot” → Confirm

(Optional) Set a bot profile picture and name

3. Enable Privileged Gateway Intents
In the “Bot” tab:

✅ Enable MESSAGE CONTENT INTENT

✅ Enable PRESENCE INTENT (optional)

✅ Enable SERVER MEMBERS INTENT (optional, not needed for your code)

4. Copy the Bot Token
Under the Bot tab, click “Reset Token” (if needed), then “Copy”

⚠️ Save it securely — treat this like a password

5. Generate an OAuth2 Invite URL
Go to OAuth2 > URL Generator

Scopes: Check bot

Bot Permissions:

✅ Send Messages

✅ Read Messages/View Channels

✅ Send Messages in DMs (default)

✅ Use Slash Commands (optional)

Copy the generated URL and open it in a browser to invite your bot to a server

6. Add Bot to a Server
Use the invite URL

Choose a server where you have Manage Server permission

Click “Authorize”

7. (Optional) Application Commands / Slash Commands
If you want to use slash commands:

Go to the “OAuth2 > URL Generator”

Add the applications.commands scope

Use a library like discord.ext.commands or discord.app_commands to register them

8. (Optional) Turn Off Public Bot
Under “Bot” > "Public Bot", turn off “Public Bot” to restrict the bot to only your servers (if needed)

---------------*fetch*---------------
