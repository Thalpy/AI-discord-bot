# DISCORD CHARACTER BOT
This code will spin up a discord bot that will chat with you as your chosen character when mentioned in a message.

This presently only works with OpenAI's API.  You will need to sign up for an account and get an API key. I'm working on free solutions but I might be slow. **This will charge you if you openai.** I'm not responsible for any charges you get. 

## Setup

### Installing requirements
```
pip install -r requirements.txt
```

### Discord Setup

- Create a file in the root directory called discord_token.txt
- Go to the Discord Developer Portal website: https://discord.com/developers/applications/
- Click on the "New Application" button to create a new application.
- Enter a name for your application and click on the "Create" button.
- In the left sidebar, click on the "Bot" tab and then click on the "Add Bot" button.
- A pop-up window will appear with a message asking if you want to add a bot to your application. Click on the "Yes, do it!" button to confirm.
- Under the "Build-A-Bot" section, you should now see your newly created bot. Click on the "Copy" button under the  "Token" section to copy your bot token to your clipboard.
- Make sure to keep your bot token secure, as anyone who has access to it can control your bot and access your Discord server.
- Paste the token into discord_token.txt and save the file. No newline, just the token.

### OpenAI Setup

- Create a file in the root directory called openai_token.txt
- Go to the OpenAI API website: https://platform.openai.com/account/api-keys
- Click create a new secret key
- Paste the token into openai_token.txt and save the file. No newline, just the token.
- You will need credits to run it.

### Bot setup

- Open discord_bot_openai.py
- Set the variables at the start (bot_name, bot_source, bot-mood)
- Fill in extra information about your character if wanted
- Open voicelines.txt and replace the example with voicelines from your character. One per line.
- Having a large amount of voicelines will make the bot more accurate, but it will also take longer to respond and use more credits.
- You can set the model if you like too - TestModels.py will show you the different models.

## Running the bot

```python
python discord_bot_openai.py
```
discord_bot_free.py can be used too, but it's pretty bad. Come back later.

## Adding the bot to your server

- Go to the Discord Developer Portal website: https://discord.com/developers/applications/
- Click on your bot
- Click on bot on the left hand side
- Heehoo funny 2FA
- Click Add Bot
- Click bot and application.read (I think??)
- In Bot Permissions which should turn up click Send Messages and Read Message History
- Copy the link and paste it into your browser
- Add it to your server
- I don't recommend making it public if the bot is using openai cause you might get charged a ton

Enjoy! No warranties or anything like that. Feel free to fork and make your own version, just credit thanks!
