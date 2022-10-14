import unittest
import main

class TestMain(unittest.TestCase):
    def test(self):
        n1=8
        n2=2
        res=main.add5(n1,n2)
        self.assertEqual(res,10)

unittest.main()