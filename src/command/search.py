from src.database_connection import search_snippet


def command_search(snippet_name):
    snippets = search_snippet(snippet_name)
    if snippets is None:
        return f'No snippets for "{snippet_name}" found.'

    # snippets is a list of tuples:
    # [('snippet1',), ('snippet2',), ...]
    return f"```\n{snippets}\n```"