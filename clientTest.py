'''
Created on Feb 2, 2023

@author: eohay
'''
import unittest

import client


class Test(unittest.TestCase):


    def testgetDataPoint(self):
      print(client.getDataPoint("ABC"))
      assert(client.getRatio(5,3)==5/3)
      assert(client.getRatio(10,0)==None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testgetDataPoint']
    unittest.main()