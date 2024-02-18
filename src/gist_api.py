"""
Module containing the Github Gist API interactions
"""
from copy import copy
from typing import Any, Optional

import requests

from src.code_snippet import CodeSnippet


GITHUB_GIST_API = 'https://api.github.com/gists'

GITHUB_GIST_HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer {token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

GITHUB_GIST_DATA_FORMAT = {
    'description': '{description}',
    'public': True,
    'files': {}
}

# TODO - Add more
LANGUAGE_TO_FILE_EXTENSION = {
    'python': 'py',
    'rust': 'rs',
    'cpp': 'cpp'
}


class GithubGistAPIError(Exception):
    """
    Exception to model an error related to the Github Gist API
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class GithubGistAPIHandler:
    """
    Class that contains all the logic for interacting with the Github Gist API.
    It relies on some
    """
    def __init__(self, token: str, url: str = GITHUB_GIST_API,
                 headers_template: Optional[dict[str, str]] = None,
                 data_template: Optional[dict] = None,
                 language_to_file_extension: Optional[dict[str, str]] = None,
                 timeout: int = 60):
        self.__token = token
        self.__url = url
        self.__headers_template = GITHUB_GIST_HEADERS if headers_template is None else headers_template
        self.__data_template = GITHUB_GIST_DATA_FORMAT if data_template is None else data_template
        self.__language_to_file_extension = LANGUAGE_TO_FILE_EXTENSION if language_to_file_extension is None else language_to_file_extension
        self.__timeout = timeout

    def upload_to_gist(self, code_snippet: CodeSnippet) -> str:
        """
        Uploads a code snippet to Github Gist.

        :param code_snippet: The code snippet to upload
        :type code_snippet: CodeSnippet
        :raises GithubGistAPIError: _description_
        :return: _description_
        :rtype: str
        """
        headers = self.__prepare_headers()
        data = self.__prepare_data(code_snippet)

        response = requests.post(self.__url, headers=headers, json=data, timeout=self.__timeout)

        if response.status_code != 201:
            message_template = 'Failed to create gist. Status code: {code}. Response: {response}'
            message = message_template.format(code=response.status_code, response=response.text)
            raise GithubGistAPIError(message)

        result_url = response.json()["html_url"]
        return result_url

    def __prepare_headers(self) -> dict[str, str]:
        headers = copy(self.__headers_template)
        headers['Authorization'] = headers['Authorization'].format(token=self.__token)

        return headers

    def __prepare_data(self, code_snippet: CodeSnippet) -> dict[str, Any]:
        data = copy(self.__data_template)

        data['description'] = data['description'].format(description=code_snippet.description)

        files = self.__prepare_files(code_snippet)
        data['files'] = files

        return data

    def __prepare_files(self, code_snippet: CodeSnippet) -> dict[str, Any]:
        file_extension = self.__language_to_file_extension[code_snippet.language.strip()]
        file_name = f'{code_snippet.name}.{file_extension}'
        code = '\n'.join(code_snippet.code)

        result = {}
        result[file_name] = {
            'content': code
        }

        return result
