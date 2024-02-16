"""
Module containing the functions to extract markdown code snippets
"""

MARKDOWN_CODE_SNIPPET_SYNTAX = '```'


def extract_code_blocks(content: list[str]) -> list[list[str]]:
    """
    Extract the code blocks from a markdown file (represented as list of strings)
    :param content: The file contents
    :return: Code blocks
    """
    code_block_indexes = [i for i, line in enumerate(content)
                          if MARKDOWN_CODE_SNIPPET_SYNTAX in line]
    code_block_bounds = zip(code_block_indexes[::2], code_block_indexes[1::2])
    code_blocks = [content[start:end+1] for start, end in code_block_bounds]

    return code_blocks
