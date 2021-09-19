from src.database_connection import find_snippet


# FIXME: % in snippet_name causes a TypeError: display_snippet() takes 1 positional argument but 2 were given
def display_snippet(snippet_name, language):
    snippet = find_snippet(snippet_name, language)

    if snippet is None:
        return 'Snippet not found!'
    return f"```{language}\n{snippet}\n```"
