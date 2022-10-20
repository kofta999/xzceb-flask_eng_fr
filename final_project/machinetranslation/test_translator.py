import unittest
from translator import english_to_french, french_to_english
class EnFrTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual('', '')

    def test2(self):
        return self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
class FrEnTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual('', '')

    def test2(self):
        return self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
if __name__ == '__main__':
    unittest.main()
   
