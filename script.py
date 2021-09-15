import hikari
import mysql.connector
from dotenv import dotenv_values

def connect_to_database(host, user, passwd, port, database, snippet_name, language):
    # connection
    myDb = mysql.connector.connect(host=host, user=user, passwd=passwd, port=port, database=database)
    cursor = myDb.cursor()

    query = (
        f"""
        SELECT snippet.name, code FROM snippet JOIN language ON snippet.language_id=language.id WHERE snippet.name LIKE '{snippet_name}' AND language.name LIKE '{language}';
        """
    )

    # we execute the operation stored in the query variable
    cursor.execute(query)

    for (name, code) in cursor:
        return f'{code}'

    cursor.close()
    myDb.close()

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

    # snippet_name and chosen programming language
    snippet_name = msg[0]
    language = msg[1]

    # respond with the snippet
    if event.content.startswith("$ snippet"):
        connection = connect_to_database(config['HOST'], config['USER'], config['PASSWD'], config['PORT'], config['DATABASE'], snippet_name, language)
        if  connection == None:
            await event.message.respond(f'Snippet not found!')
        else:
            await event.message.respond(f"""```{language}\n{connection}\n```""")

bot.run()