"""
Main program module
"""
import os
import sys

from dotenv import load_dotenv

from src.cli import parse_args, setup_cli
from src.code_snippet import CodeSnippet
from src.gist_api import GithubGistAPIError, GithubGistAPIHandler
from src.markdown_extract import extract_code_blocks, extract_code_block_language
from src.ui import preview_raw_code_snippet, read_user_input, show_message

if __name__ == "__main__":
    load_dotenv()
    parser = setup_cli()
    arguments = parse_args(parser)

    # Generally, should not happen, but still...
    if 'file_path' not in arguments:
        show_message("Error: file_path not found in parsed arguments. Check CLI")
        sys.exit(1)

    filepath = arguments['file_path']

    if not os.path.isfile(filepath):
        show_message(f"Error: File {filepath} not found")
        sys.exit(1)

    show_message(filepath)

    try:
        with open(filepath, mode='r', encoding='utf-8') as file_pointer:
            content = file_pointer.readlines()
    except IOError as exc:
        show_message(f'Error: Cannot read file {filepath}. Exception: {exc}')
        sys.exit(1)

    code_blocks = extract_code_blocks(content)

    code_snippets = []
    for i, code_block in enumerate(code_blocks, start=1):
        show_message(f'Showing snippet {i}')
        preview_raw_code_snippet(code_block)

        name = read_user_input('Please enter a file name:')
        language = extract_code_block_language(code_block[0])
        description = read_user_input('Please enter a description:')

        code_snippet = CodeSnippet(name, code_block, language, description)
        code_snippets.append(code_snippet)

    gist_token = os.environ['GITHUB_GIST_TOKEN']
    gist_api = GithubGistAPIHandler(gist_token)

    for code_snippet in code_snippets:
        try:
            result_url = gist_api.convert_to_gist(code_snippet)
        except GithubGistAPIError as exc:
            show_message(exc)
            continue

        show_message(result_url)
