import os
from dotenv import load_dotenv
import discord
import deepl
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
AUTH_KEY = os.getenv("DEEPL_AUTHKEY")
channel1 = os.getenv("MAIN_CHANNEL")
channel2 = os.getenv("TRANSLATEDCHANNEL")
channel1 = int(channel1)
channel2 = int(channel2)
print(channel1 + channel2)
translator = deepl.Translator(AUTH_KEY)

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Your bot is called: {client.user.name}')

@client.event
async def on_message(message):
    if message.channel.id == channel1: # channel it gets the messages from
        channel = client.get_channel(channel2) # channel it sends the translated messages to
        author_name = message.author.name
        result = translator.translate_text(message.content, target_lang="EN-GB")
        content = f"{author_name}: {result}"

        # sends the message and print it
        print(f"Sending message: {result}")
        await channel.send(content)


# start the bot
client.run(TOKEN)