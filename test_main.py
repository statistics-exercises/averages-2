import scipy.stats as st
import unittest
from main import * 

class UnitTests(unittest.TestCase) :
    def test_uniform_rv(self): 
        for i in range(-2,3) : 
            for j in range(1,5) :
                a, b, mean = i - j, i + j, 0
                for k in range(100) : mean = mean + uniform(a,b)
                mean = mean / 100
                var = 1/12*(b-a)*(b-a)
                bar = np.sqrt(var/100)*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean - 0.5*(b+a) )<bar, "your funciton does not sample from the correct statistical distribution" )
