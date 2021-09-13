import discord
from discord.ext import commands
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('Our bot is ready')

# testing. . .
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$snippet_test'):
        msg = message.content.split()
        await message.channel.send(f'Looking for: "{msg[1]}" in "{msg[2]}"')

client.run(config['BOT_TOKEN'])