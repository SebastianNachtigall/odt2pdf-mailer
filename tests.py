import unittest
class StringMethodstest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('python'.upper(), 'PYTHON')
    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('python'.isupper())
    def test_split(self):
        s = 'hello python'
        self.assertEqual(s.split(), ['hello', 'python'])
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()