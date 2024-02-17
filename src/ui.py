"""
A module mainly for future development, if I want a fancier UI
"""

def preview_raw_code_snippet(code_snippet: list[str]):
    for line in code_snippet:
        print(line)


def show_message(message: str):
    print(message)


def read_user_input(prompt: str = '') -> str:
    return input(prompt)