import random

import mysql.connector
# noinspection PyPackages
from .config import config


def find_snippet(name, language):
    my_db = mysql.connector.connect(host=config['HOST'], user=config['USER'], passwd=config['PASSWD'],
                                    port=config['PORT'], database=config['DATABASE'])
    cursor = my_db.cursor(prepared=True)

    query = """SELECT code FROM snippet
    JOIN language ON snippet.language_id=language.id
    WHERE snippet.name=%s AND language.name=%s;"""
    parameters = (name.lower(), language.lower())
    cursor.execute(query, parameters)

    result = cursor.fetchall()

    cursor.close()
    my_db.close()

    if len(result) == 0:
        return None

    # result is a list of tuples
    return random.choice(result)[0]


def connect_to_database(command, query):
    # connection
    my_db = mysql.connector.connect(host=config['HOST'], user=config['USER'], passwd=config['PASSWD'],
                                    port=config['PORT'], database=config['DATABASE'])
    cursor = my_db.cursor()

    if command == "$ list":
        # we execute the operation stored in the query variable
        cursor.execute(query)

        # This method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
        listed_snippets = cursor.fetchall()

        # return all of the snippets written in a specific language
        for listed_snippet in listed_snippets:
            return listed_snippet[0]

    elif command == "$ search":
        # we execute the operation stored in the query variable
        cursor.execute(query)

        # This method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
        listed_languages = cursor.fetchall()

        # return all of the languages that has user's snippet
        for listed_language in listed_languages:
            return listed_language[0]

    cursor.close()
    my_db.close()
