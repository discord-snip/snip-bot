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
    parameters = [name.lower(), language.lower()]
    cursor.execute(query, parameters)

    result = cursor.fetchall()

    cursor.close()
    my_db.close()

    if len(result) == 0:
        return None

    # result is a list of tuples
    return random.choice(result)[0]


def list_snippets(language):
    my_db = mysql.connector.connect(host=config['HOST'], user=config['USER'], passwd=config['PASSWD'],
                                    port=config['PORT'], database=config['DATABASE'])
    cursor = my_db.cursor(prepared=True)

    query = """SELECT snippet.name FROM snippet
    JOIN language ON snippet.language_id=language.id
    WHERE language.name=%s;"""
    parameters = [language.lower()]
    cursor.execute(query, parameters)

    result = cursor.fetchall()

    cursor.close()
    my_db.close()

    if len(result) == 0:
        return None

    # result is a list of tuples
    return result


def search_snippet(name):
    my_db = mysql.connector.connect(host=config['HOST'], user=config['USER'], passwd=config['PASSWD'],
                                    port=config['PORT'], database=config['DATABASE'])
    cursor = my_db.cursor()
    query = """SELECT snippet.name, language.name FROM snippet
        JOIN language ON snippet.language_id=language.id
        WHERE snippet.name LIKE %s;"""
    parameters = [f"%{name.lower()}%"]
    cursor.execute(query, parameters)

    result = cursor.fetchall()

    cursor.close()
    my_db.close()

    if len(result) == 0:
        return None

    # result is a list of tuples
    return result
