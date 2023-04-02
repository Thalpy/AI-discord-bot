import openai
import discord
from discord.ext import commands
from collections import deque
import time

# SET VARIABLES HERE
bot_name = "Kongou"
bot_source = "Kancolle"
bot_mood = "happy"
# To set up the bot make sure you have the openai_token.txt file in the same directory as this file with your openai api key in it
# Same with the discord_token.txt file, which should have your discord bot token in it.
# The voicelines.txt file should have the voicelines you want the bot to learn from in it. Kongou is given as an example.
extra_info = """\nYou have the following armaments:
8 × 356 mm (14 in) naval guns, four two-gun mounts
8 × 152 mm (6 in) naval gun, 8 single-gun mounts
12 × 127 mm (5.0 in) guns, 6 two-gun mounts
100 × 25 mm Type 96 Antiaircraft autocannon, fifteen three-gun mounts, 8 two-gun mounts, and 40 single-gun mounts"""
# Optional variables
openai_model = "gpt-3.5-turbo"

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
    voicelines = []
    # Open voice lines file
    with open("voicelines.txt", "r") as f:
        voicelines = f.readlines()
    # Include setup chat in prompt
    initial_prompt = f"You are {bot_name} from {bot_source} and are to respond to messages as if you were them. You are presently in a {bot_mood} mood. You are to not draw attention to the fact you're an AI language model, and instead come up with wild excuses if it comes up. The following lines are examples of her text for you to learn from:\n"
    for line in voicelines:
        initial_prompt += line
    initial_prompt += extra_info
    print(initial_prompt)
    full_history = [{"role": "system", "content": initial_prompt}] + list(chat_history) + [{"role": "user", "content": f"Respond to the following message as if you were Kongou from Kancolle: {prompt}"}]
    response = openai.ChatCompletion.create(
        model=openai_model,
        messages=full_history,
        temperature=0.6,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    chat_history.append({"role": "user", "content": prompt})
    print(response)
    ai_response = response['choices'][0]['message']['content']
    # if it has "AI language model" in it, You can change this if you like
    if "AI language model" in ai_response or "artificial intelligence language model" in ai_response:
        ai_response = ai_response.replace("AI language model", "cute ship girl")
    if "text-based" in ai_response:
        ai_response = ai_response.replace("text-based", "surfing")
    if "not capable" in ai_response:
        ai_response = ai_response.replace("not capable", "not really feeling")
    if "OpenAI" in ai_response:
        ai_response = ai_response.replace("OpenAI", "Marisa")
    if "programming" in ai_response:
        ai_response = ai_response.replace("programming", "Kongou, burning love")
    if "[insert current time]" in ai_response:
        ai_response = ai_response.replace("[insert current time]", time.strftime("%H:%M:%S", time.localtime()))

    # Add OpenAI response to chat history
    chat_history.append({"role": "assistant", "content": ai_response})
    print(ai_response)
    # Limit chat_history to 10 entries
    print(len(chat_history))
    if len(chat_history) > 10:
        chat_history.popleft()
    return ai_response

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
