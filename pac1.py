import math
def QUADRATIC_EQN(a,b,c):
       try:
         res1 =(-b+math.sqrt(b**2 - 4*a*c))/2*a
         return res1
       except ValueError:
             print("There is some error")

    
