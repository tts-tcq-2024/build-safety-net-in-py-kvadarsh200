import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

     def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_letter(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    def test_common_names(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Johnson"), "J525")

    def test_repeated_characters(self):
        self.assertEqual(generate_soundex("Tennessee"), "T520")
        self.assertEqual(generate_soundex("Lee"), "L000")

    def test_mixed_case(self):
        self.assertEqual(generate_soundex("McDonald"), "M235")
        self.assertEqual(generate_soundex("MacDonald"), "M235")

    def test_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("O'Brien"), "O165")
        self.assertEqual(generate_soundex("D'Angelo"), "D524")

    def test_edge_cases(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("E"), "E000")
        self.assertEqual(generate_soundex("Y"), "Y000")
        self.assertEqual(generate_soundex("!@#$"), "!000")
    
if __name__ == '__main__':
    unittest.main()
