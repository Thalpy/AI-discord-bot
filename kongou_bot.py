import os
import openai
import discord
from discord.ext import commands

# get the openai api key from the openai api key file
with open("openai_api_key.txt", "r") as f:
    openai.api_key = f.read()

# Set up Discord bot
bot = commands.Bot(command_prefix="!")

def generate_kongou_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Respond to the following message as if you were Kongou from Kancolle in a seductful mood: {prompt}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the bot is mentioned in the message
    if bot.user in message.mentions:
        prompt = message.content.replace(f"<@!{bot.user.id}>", "").strip()
        kongou_response = generate_kongou_response(prompt)
        await message.channel.send(kongou_response)

    await bot.process_commands(message)

# get the discord token from the discord token file
with open("discord_token.txt", "r") as f:
    discord_token = f.read()

bot.run(discord_token)
