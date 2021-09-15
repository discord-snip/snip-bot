import hikari
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

bot = hikari.GatewayBot(token=config['BOT_TOKEN'])

@bot.listen()
async def display_snippet(event: hikari.GuildMessageCreateEvent):
    # If a non-bot user sends a message "$snippet", respond with "Looking for /code/ in /language/"
    # We check if there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    msg = event.content.split()[1:]

    if event.content.startswith("$snippet"):
        await event.message.respond(f'Looking for {msg[0]} in {msg[1]}')

bot.run()