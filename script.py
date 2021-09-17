import hikari
from snippet import display_chosen_snippet
from list_snippets import list_language_snippets
from search import search_snippet
from dotenv import dotenv_values

# config .env .env.local
config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

# hikari stuff
bot = hikari.GatewayBot(token=config['BOT_TOKEN'])

@bot.listen()
async def display_snippet(event: hikari.GuildMessageCreateEvent):
    # If a non-bot user sends a message "$snippet", respond with "Looking for /code/ in /language/"
    # We check if there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    # user's message
    msg = event.content.split()[2:]

    if event.content.startswith("$ snippet") and len(msg) == 2:
        snippet_name = msg[0]
        snippet_language = msg[1]

        await event.message.respond(display_chosen_snippet(snippet_name, snippet_language))
    elif event.content.startswith("$ list") and len(msg) == 1:
        listed_language = msg[0]
        await event.message.respond(list_language_snippets(listed_language))
    elif event.content.startswith("$ search") and len(msg) == 1:
        listed_snippet = msg[0]
        await event.message.respond(search_snippet(listed_snippet))
    else:
        if event.content.startswith("$"):
            await event.message.respond("Unknown command :-(")

bot.run()