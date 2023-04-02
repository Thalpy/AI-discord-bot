import openai
import discord
from discord.ext import commands


# SET VARIABLES HERE
bot_name = "Kongou"
bot_source = "Kancolle"
bot_mood = "happy"

# GPT MODEL SETUP

# GPT-2

from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# GPT-J-6B

# from transformers import pipeline

# generator = pipeline('text-generation', model='EleutherAI/gpt-j-6B', device=0)

# END GPT MODEL SETUP

# Memory
chat_history = []
max_history_len = 10
setup_chat = []

# Set up Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_kongou_response_gptj(prompt):
    # in progress
    response = generator(prompt, max_length=1000, do_sample=True, temperature=0.7)

    return response

def generate_kongou_response_gpt2(prompt):
    full_prompt = f"Respond to the following message as if you were {bot_name} from {bot_source}: {prompt}"
    input_ids = tokenizer.encode(full_prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    # remove the prompt from the response
    response = response.replace(full_prompt, "")
    print(response)
    return response.strip()


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the bot is mentioned in the message
    if bot.user in message.mentions:
        prompt = message.content.replace(f"<@!{bot.user.id}>", "").strip()
        kongou_response = generate_kongou_response_openai_gpt2(prompt)
        await message.channel.send(kongou_response)

    await bot.process_commands(message)

# get the discord token from the discord token file
with open("discord_token.txt", "r") as f:
    discord_token = f.read()

bot.run(discord_token)
