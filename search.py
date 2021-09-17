from database_connection import connect_to_database

def search_snippet(snippet_name):
    query = (
        f"""
        SELECT language.name FROM snippet JOIN language ON snippet.language_id=language.id WHERE snippet.name LIKE '{snippet_name}';
        """
    )

    connection = connect_to_database("$ search", query)

    if connection == None:
        return f'No languages has {snippet_name} snippet.'
    return f"""```\n{connection}\n```"""