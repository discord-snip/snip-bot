from database_connection import connect_to_database

def list_language_snippets(language):
    query = (
        f"""
        SELECT snippet.name FROM snippet JOIN language ON snippet.language_id=language.id WHERE language.name LIKE '{language}';
        """
    )

    connection = connect_to_database("$ list", query)
    if connection == None:
        return f'No snippets for {language} found.'
    return f"""```\n{connection}\n```"""