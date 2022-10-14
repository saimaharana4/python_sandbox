import unittest
import main

class TestMain(unittest.TestCase):
    def test(self):
        n1=8
        n2=2
        res=main.add5(n1,n2)
        self.assertEqual(res,10)

    def test2(self):
        n1='fcdhj'
        n2='fdhyjgchg'
        res=main.add5(n1,n2)
        self.assertIsInstance(res,ValueError)

    def test3(self):
        n1= None
        n2= None
        res=main.add5(n1,n2)
        self.assertEqual(res,"Enter a no")

    def test4(self):
        n1= ""
        n2= ""
        res=main.add5(n1,n2)
        self.assertIsInstance(res,(AssertionError, ValueError))

unittest.main()