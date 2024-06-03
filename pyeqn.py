import math
#Fuction for Quadratic equation
def QUADRATIC_EQN(a,b,c):
       try:
         res1 =(-b+math.sqrt(b**2 - 4*a*c))/2*a
         res2 =(-b-math.sqrt(b**2 - 4*a*c))/2*a
         return (res1,res2)
       except ValueError:
             print("The equation has complex root")



    
