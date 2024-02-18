"""
Module containing the CLI interface of the app.
"""

from argparse import ArgumentParser
from typing import Any


def setup_cli() -> ArgumentParser:
    """
    Sets up the command line interface

    :return: The CLI parser
    :rtype: ArgumentParser
    """
    parser = ArgumentParser(prog='markdown2gist',
                            description='Convert code snippets from markdown into gists')

    parser.add_argument('file_path', type=str)

    return parser


def parse_args(parser: ArgumentParser) -> dict[str, Any]:
    """
    Parses and returns the CLI arguments as a dictionary

    :param parser: The argument parser object
    :type parser: ArgumentParser
    :return: Dictionary containing the arguments
    :rtype: Dictionary
    """
    return parser.parse_args().__dict__
