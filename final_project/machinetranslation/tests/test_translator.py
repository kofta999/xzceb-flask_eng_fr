import unittest
from translator import english_to_french, french_to_english

class EnFrTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual('', '')

    def test2(self):
        return self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test3(self):
        return self.assertNotEqual(english_to_french('Hi'), 'Ju')
    
class FrEnTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual('', '')

    def test2(self):
        return self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test3(self):
        return self.assertNotEqual(english_to_french('Ju'), 'Hi')
    
if __name__ == '__main__':
    unittest.main()