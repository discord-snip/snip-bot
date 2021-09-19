from src.database_connection import list_snippets


def command_list(language):
    snippets = list_snippets(language)
    if snippets is None:
        return f'No snippets for {language} found.'

    # snippets is a list of tuples:
    # [('snippet1',), ('snippet2',), ...]
    return f"```\n{snippets}\n```"
