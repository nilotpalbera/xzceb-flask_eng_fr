import unittest
from translator import englishToFrench, frenchToEnglish

class TEST_TRANSLATION(unittest.TestCase):
    def test_cases(self):
        #en-fr
        self.assertEqual(englishToFrench('Hi'), 'Salut')
        self.assertEqual(englishToFrench('English to French'), 'Anglais vers français')

        #fr-en 
        self.assertEqual(frenchToEnglish('Salut'), 'Hi')
        self.assertEqual(frenchToEnglish('français vers anglais'), 'French to English')

        #None values
        try:
            self.assertEqual(englishToFrench(None), '')
            self.assertEqual(frenchToEnglish(None), '')
        except ValueError as err:
            print(err)

        #Hello and Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hello')

        



unittest.main()