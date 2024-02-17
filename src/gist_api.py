"""
Module containing the Github Gist API interactions
"""
import requests

from copy import copy
from typing import Any

from src.code_snippet import CodeSnippet


GITHUB_GIST_API = 'https://api.github.com/gists'

GITHUB_GIST_HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer {token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

GITHUB_GIST_DATA_FORMAT = {
    'description': '{description}',
    'public': False,
    'files': {}
}

# TODO - Add more
LANGUAGE_TO_FILE_EXTENSION = {
    'python': 'py',
    'rust': '.rs'
}

class GithubGistAPIError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class GithubGistAPIHandler:
    def __init__(self, token: str, url: str = GITHUB_GIST_API,
                 headers_template: dict[str, str] = GITHUB_GIST_HEADERS,
                 data_template: dict = GITHUB_GIST_DATA_FORMAT,
                 language_to_file_extension: dict[str, str] = LANGUAGE_TO_FILE_EXTENSION):
        self.__token = token
        self.__url = url
        self.__headers_template = headers_template
        self.__data_template = data_template
        self.__language_to_file_extension = language_to_file_extension

    def convert_to_gist(self, code_snippet: CodeSnippet) -> str:
        headers = self.__prepare_headers()
        data = self.__prepare_data()

        response = requests.post(self.__url, headers=headers, json=data)

        if response.status_code != 201:
            raise GithubGistAPIError(f'Failed to create gist. Status code: {response.status_code}. Response: {response.text}')

        result_url = response.json()["html_url"]
        return result_url

    def __prepare_headers(self) -> dict[str, str]:
        headers = copy(self.__headers_template)
        headers['Authorization'] = headers['Authorization'].format(self.__token)

        return headers

    def __prepare_data(self, code_snippet: CodeSnippet) -> dict[str, Any]:
        data = copy(self.__data_template)

        data['description'] = data['description'].format(code_snippet.description)

        files = self.__prepare_files(code_snippet)
        data['files'] = files

        return data
    
    def __prepare_files(self, code_snippet: CodeSnippet) -> dict[str, Any]:
        file_extension = self.__language_to_file_extension[code_snippet.language]
        file_name = f'{code_snippet.name}.{file_extension}'
        code = '\n'.join(code_snippet.code)

        result = {}
        result[file_name] = {
            'content': code
        }

        return result
GITHUB_GIST_FILE_FORMAT = {
    '{filename}': { 
        'content': '{code}'
    }
}


def prepare_data(filename: str, code: list[str], description: str = '', base: dict[str, Any] = GITHUB_GIST_HEADERS) -> dict[str, Any]:
    data = copy(base)
    data['description'] = data['description'].format(description)

    files = copy(data['files'])

    files[]
    data['files'] = files
    return data