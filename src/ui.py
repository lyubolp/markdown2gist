"""
A module mainly for future development, if I want a fancier UI
"""


def preview_raw_code_snippet(code_snippet: list[str]):
    """
    Show raw code snippet to the user

    :param code_snippet: The unprocessed code snippet
    :type code_snippet: list[str]
    """
    for line in code_snippet:
        print(line)


def show_message(message: str):
    """
    Show a message to the user

    :param message: Message to be shown
    :type message: str
    """
    print(message)


def read_user_input(prompt: str = '') -> str:
    """
    Prompt a user for input.

    :param prompt: The prompt to be shown when asking for input, defaults to ''
    :type prompt: str, optional
    :return: _description_
    :rtype: str
    """
    return input(prompt)
