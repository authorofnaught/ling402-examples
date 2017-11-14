from foo import reduplicate
from foo import convert
import unittest

class TestFoo(unittest.TestCase):

    def test_catcat(self):
        expected="cat-cat"
        actual=reduplicate("cat")
        self.assertEqual(actual, expected)

    def test_dogdog(self):
        expected="dog-dog"
        actual=reduplicate("dog")
        self.assertEqual(actual, expected)

    def test_klingon1(self):
        expected="qʰɑʔpʰlɑx"
        actual=convert("qa'plaH")
        self.assertEqual(actual,expected)

    def test_klingon2(self):
        expected = "t͡ʃ" +"ɑʔpʰlɑx"
        actual=convert("cha'plaH")
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main()

