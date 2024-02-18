"""
Module containing a model for the code snippet
"""

from typing import Optional


class CodeSnippet:
    """
    Class to model a snippet of code. 
    Contains the name of the snippet, the code, the language and optional description.
    """
    def __init__(self, name: str, code: str, language: str, description: Optional[str] = None):
        self.__name = name
        self.__code = code[1:-1]  # Remove the start and end of the codeblock
        self.__language = language
        self.__description = description

    @property
    def name(self) -> str:
        """
        Returns the name of the snippet
        :rtype: str
        """
        return self.__name

    @property
    def code(self) -> str:
        """
        Returns the code of the snippet
        :rtype: str
        """
        return self.__code

    @property
    def language(self) -> str:
        """
        Returns the language of the snippets
        :rtype: str
        """
        return self.__language

    @property
    def description(self) -> Optional[str]:
        """
        Returns the description of the snippet
        :rtype: Optional[str]
        """
        return self.__description
