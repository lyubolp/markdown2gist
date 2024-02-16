import unittest

from src.markdown_extract import extract_code_blocks


class TestExtractCodeBlock(unittest.TestCase):
    """
    Tests for the extract_code_blocks.

    The structure of a markdown file (from the perspective of this function)
    contain code and non-code. This expressed as a regex could look something like this:

    ((NC*)(C*))* - each element can appear 0 or multiple times.

    The tests coverring this could be:
    0-0-0
    0-1-0
    0-1-1
    0-2-0

    1-0-0
    1-1-0
    1-1-1
    1-2-0

    Code snippets can be with or without the language specified

    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.__non_code_snippet = ['# Header 1', 'Body 1', '## Header 2', '**Body 2**']
        cls.__code_snippet = ['```', 'print("Hello world")', 'def foo():',
                              '\tprint("foo")', '', 'foo()', '```']

        return super().setUpClass()

    def __generate_test_content(self, non_code_first_count: int, code_count: int, 
                                non_code_second_count: int) -> list[str]:
        content = self.__non_code_snippet * non_code_first_count
        content += self.__code_snippet * code_count
        content += self.__non_code_snippet * non_code_second_count

        return content

    def __base_test(self, non_code_first_count: int, code_count: int, non_code_second_count: int):
        # Arrange
        content = self.__generate_test_content(non_code_first_count, code_count,
                                               non_code_second_count)
        expected = [self.__code_snippet for _ in range(code_count)]

        # Act
        actual = extract_code_blocks(content)

        # Assert
        self.assertEqual(expected, actual)

    def test_01_zero_non_code_zero_code_zero_non_code(self):
        self.__base_test(0, 0, 0)

    def test_02_zero_non_code_one_code_zero_non_code(self):
        self.__base_test(0, 1, 0)

    def test_03_zero_non_code_one_code_one_non_code(self):
        self.__base_test(0, 1, 1)

    def test_04_zero_non_code_two_code_zero_non_code(self):
        self.__base_test(0, 2, 0)

    def test_05_one_non_code_zero_code_zero_non_code(self):
        self.__base_test(1, 0, 0)

    def test_06_one_non_code_one_code_zero_non_code(self):
        self.__base_test(1, 1, 0)

    def test_07_one_non_code_one_code_zero_one_code(self):
        self.__base_test(1, 1, 1)

    def test_08_one_non_code_two_code_zero_non_code(self):
        self.__base_test(1, 2, 0)