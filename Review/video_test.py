import unittest
import time
import subprocess
import os

class video_test(unittest.TestCase):
    def test(self):
    	count = 0
    	subprocess.call("python api.py",shell = True)
    	for file in os.listdir('.'):
        	if file.endswith('.mp4'):
        		count = 1
    	self.assertEqual(count,1)

if __name__ == '__main__':
    unittest.main()