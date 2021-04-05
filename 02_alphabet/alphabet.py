"""  
There is an alphabet which has the following characteristics:
- language
- letters

Print all the letters
Count letters.
"""


class Alphabet():

    def __init__(self, language: str, letters: str):
        if type(letters) != str:
            raise Exception('Unexpected input for letters')

        if type(language) != str:
            raise Exception('Unexpected input for language')

        self.language = language
        self.letters = letters

    def print_letters(self) -> str:
        return self.letters

    def count_letters(self) -> int:
        return len(self.letters)
