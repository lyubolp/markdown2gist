"""
Module containing the CLI interface of the app.
"""

from argparse import ArgumentParser


def setup_cli() -> ArgumentParser:
    parser = ArgumentParser(prog='markdown2gist',
                            description='Convert code snippets from markdown into gists')

    parser.add_argument('file_path', type=str)

    return parser


def parse_args(parser: ArgumentParser):
    return parser.parse_args().__dict__
