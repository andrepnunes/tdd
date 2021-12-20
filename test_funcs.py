import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min(self):
        self.assertEqual(funcs.min(1,2),1)
        self.assertEqual(funcs.min(2,1),1)
        self.assertEqual(funcs.min(3,3),3)
        self.assertEqual(funcs.min(-2,-1),-2)
        self.assertEqual(funcs.min(-1,-2),-2)
        
if __name__ == '__main__':
    unittest.main()
