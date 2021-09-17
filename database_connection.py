import mysql.connector
from dotenv import dotenv_values

# config .env .env.local
config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

def connect_to_database(command, query):
    # connection
    myDb = mysql.connector.connect(host=config['HOST'], user=config['USER'], passwd=config['PASSWD'], port=config['PORT'], database=config['DATABASE'])
    cursor = myDb.cursor()


    if command == "$ snippet":
        # we execute the operation stored in the query variable
        cursor.execute(query)

        for (name, code) in cursor:
            return f'{code}'

    elif command == "$ list":
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
    myDb.close()