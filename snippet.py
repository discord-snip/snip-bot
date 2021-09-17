from database_connection import connect_to_database

def display_chosen_snippet(snippet_name, language):
    query = (
        f"""
        SELECT snippet.name, code FROM snippet JOIN language ON snippet.language_id=language.id WHERE snippet.name LIKE '{snippet_name}' AND language.name LIKE '{language}';
        """
    )

    connection = connect_to_database("$ snippet", query)

    if connection == None:
        return f'Snippet not found!'
    return f"""```{language}\n{connection}\n```"""