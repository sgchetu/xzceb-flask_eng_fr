import unittest
from translator import english_to_french
from translator import french_to_english

class test_translation(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e2(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Angry')
    def test_f2e3(self):
        self.assertNotEqual(french_to_english("None"), '')
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_e2f1(self):
        self.assertNotEqual(english_to_french('Sad'),'Bonjour')
    def test_e2f3(self):
        self.assertNotEqual(english_to_french("None"), '')
if __name__ == "__main__":unittest.main()
