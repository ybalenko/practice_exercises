import unittest
import string
from alphabet import Alphabet


class AlphabetTestCase(unittest.TestCase):

    def test_print_letters_from_given_eng_alphabet(self):
        ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lang = Alphabet('English', ascii_uppercase)
        res = lang.print_letters()
        self.assertEqual(res, ascii_uppercase)

    def test_print_letters_from_given_ru_alphabet(self):
        ascii_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        lang = Alphabet('Russian', ascii_lowercase)
        res = lang.print_letters()
        self.assertEqual(res, ascii_lowercase)

    def test_given_alphabet_as_int_returns_error(self):
        test_data = 123456
        try:
            Alphabet('Test', test_data)
            self.assertFalse(True, "Expected exception")
        except:
            return

    def test_given_alphabet_as_emoji_counts(self):
        test_data = '😁'
        lang = Alphabet('😁', test_data)
        res = lang.count_letters()
        self.assertTrue(res, test_data)

    def test_count_letters_from_given_Eng_alphabet(self):
        ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lang = Alphabet('English', ascii_uppercase)
        res = lang.count_letters()
        self.assertEqual(res, len(ascii_uppercase))

    def test_given_empty_str_for_alphabet_returns_count_0(self):
        test_data = ''
        lang = Alphabet('Test', test_data)
        res = lang.count_letters()
        self.assertEqual(0, res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
