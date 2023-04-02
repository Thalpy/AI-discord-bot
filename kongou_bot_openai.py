import os
import openai
import discord
from discord.ext import commands
from collections import deque

# GPT MODEL SETUP
# OpenAI GPT-4

# get the openai api key from the openai api key file
with open("openai_token.txt", "r") as f:
    openai.api_key = f.read()
# END GPT MODEL SETUP

# Memory
chat_history = deque(maxlen=10)
setup_chat = []

# Set up Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def generate_kongou_response_openai_gpt3_5(prompt):
    chat_history.append({"role": "user", "content": prompt})
    # Include setup chat in prompt
    full_history = setup_chat + list(chat_history)

    # Combine chat history into a single prompt
    full_prompt = "The following is a conversation between a user and an AI assistant.\n"
    for role, text in full_history:
        full_prompt += f"{role}: {text}\n"
    print(full_prompt)

    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=formatted_prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    ai_response = response.choices[0].text.strip()
    # Add OpenAI response to chat history
    chat_history.append({"role": "assistant", "content": ai_response})
    print(ai_response)
    return ai_response

def set_up_discord_bot():
    prompt = f"You are Kongou from Kancolle, please respond as such for the duration of the conversation."
    setup_chat.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    ai_response = response.choices[0].text.strip()
    # Add OpenAI response to chat history
    setup_chat.append({"role": "assistant", "content": ai_response})
    print(setup_chat)
    return 

set_up_discord_bot()
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the bot is mentioned in the message
    if bot.user in message.mentions:
        prompt = message.content.replace(f"<@!{bot.user.id}>", "").strip()
        kongou_response = generate_kongou_response_openai_gpt3_5(prompt)
        await message.channel.send(kongou_response)

    await bot.process_commands(message)

# get the discord token from the discord token file
with open("discord_token.txt", "r") as f:
    discord_token = f.read()

bot.run(discord_token)