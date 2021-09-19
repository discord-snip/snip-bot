from src.database_connection import list_snippets

def list_language_snippets(language):
    snippets = list_snippets(language)
    if snippets == None:
        return f'No snippets for {language} found.'

    # snippets is a list of tuples:
    # [('snippet1',), ('snippet2',), ...]
    return f"```\n{snippets}\n```"
