import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

def wallis(n):
    if n==0:
        return 2
    else:
        return ((4*n**2)/((4*n**2)-1))*wallis(n-1)
    

class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
 
def monte_carlo(darts):

    def circledots(darts):
          inCircle = 0
          for dot in range(1,darts+1):
               x = random.random()
               y = random.random()
               if (x*x + y*y)**0.5 <= 1.0:
                    inCircle += 1
          #Counting for four Quadrants
          return 4*(inCircle/float(darts))

    def squaredots(darts):
          insquare = 0
          for dot in range(1,darts+1):
               x = random.random()
               y = random.random()
               if 0<=x<=1 and 0<=y<=1:
                    insquare+=1
          #Counting for four Quadrants       
          return 4*(insquare/float(darts))

    return 4*(circledots(darts)/squaredots(darts))      
    
if __name__ == "__main__":
    unittest.main()
