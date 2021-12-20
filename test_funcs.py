import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min(self):
        self.assertEqual(funcs.min(1,2),1)
        self.assertEqual(funcs.min(2,1),1)
        self.assertEqual(funcs.min(3,3),3)
        self.assertEqual(funcs.min(-2,-1),-2)
        self.assertEqual(funcs.min(-1,-2),-2)

    def test_avg(self):
        self.assertEqual(funcs.avg([ -1,  0]),-0.5)
        self.assertEqual(funcs.avg([  0,  0, 0]),0)
        self.assertEqual(funcs.avg([  1,  2, 3]),2)
        self.assertEqual(funcs.avg([ -1, -4, 2, 1]),-0.5)

    def test_med(self):
        self.assertEqual(funcs.med([ -1,  0]),-0.5)
        self.assertEqual(funcs.med([  0,  0, 0]),0)
        self.assertEqual(funcs.med([  1,  2, 3]),2)
        self.assertEqual(funcs.med([ -1, -4, 2, 1]), 0)

    def test_std(self):
        self.assertEqual(funcs.std([ -1,  0]),0.5)
        self.assertEqual(funcs.std([  0,  0, 0]),0)
        self.assertEqual(funcs.std([  1, 3, 5, 5, 6, 6 ,6, 7, 12]),3)
        self.assertEqual(funcs.std([ 3, 3, 3, 4, 4, 5, 5, 7, 11, 15]), 4)
        
if __name__ == '__main__':
    unittest.main()
