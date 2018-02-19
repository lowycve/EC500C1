import unittest
import time
import subprocess

class time_test(unittest.TestCase):
    def test(self):
        start = time.clock()
        subprocess.call("python api.py",shell = True)
        stop = time.clock()
        t = stop - start
        self.assertLess(t,1)

if __name__ == '__main__':
    unittest.main()