import unittest
import time
import subprocess
import os

class nonphoto_test(unittest.TestCase):
    def test(self):
    	count = 0
    	subprocess.call("python api.py",shell = True)
    	for file in os.listdir('.'):
        	if file.endswith('.jpg'):
        		count = count + 1
    	self.assertEqual(count,0)

if __name__ == '__main__':
    unittest.main()