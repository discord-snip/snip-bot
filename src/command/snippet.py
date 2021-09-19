from src.database_connection import find_snippet


def display_snippet(snippet_name, language):
    snippet = find_snippet(snippet_name, language)

    if snippet is None:
        return 'Snippet not found!'
    return f"```{language}\n{snippet}\n```"
