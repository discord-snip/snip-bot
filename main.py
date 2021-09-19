from src.config import config
import hikari
from src.command.snippet import display_snippet
from src.command.list_snippets import list_language_snippets
from src.command.search import search_snippet


if __name__ == '__main__':

    bot = hikari.GatewayBot(token=config['BOT_TOKEN'])


    @bot.listen()
    async def display_snippet(event: hikari.GuildMessageCreateEvent):
        # If a non-bot user sends a message "$snippet", respond with "Looking for /code/ in /language/"
        # We check if there is actually content first, if no message content exists,
        # we would get `None' here.
        if event.is_bot or not event.content:
            return

        # user's message
        msg = event.content.split()
        trigger = msg[0]
        command = msg[1]
        msg = msg[2:]

        if trigger != "$":
            return

        if command == "snippet" and len(msg) == 2:
            snippet_name = msg[0]
            snippet_language = msg[1]
            await event.message.respond(display_snippet(snippet_name, snippet_language))
        elif command == "list" and len(msg) == 1:
            listed_language = msg[0]
            await event.message.respond(list_language_snippets(listed_language))
        elif command == "search" and len(msg) == 1:
            listed_snippet = msg[0]
            await event.message.respond(search_snippet(listed_snippet))
        else:
            await event.message.respond("Unknown command :confused:")


    bot.run()
