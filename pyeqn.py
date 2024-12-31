'''
* Jothi Prakasam
'''
import math
import matplotlib.pyplot as plt
#This package has been maintained by JOTHI PRAKASAM R
# Function for solving a quadratic equation
def QUADRATIC_EQN(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("The equation has complex roots")
        res1 = (-b + math.sqrt(discriminant)) / (2*a)
        res2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (res1, res2)
    except ValueError:
        print("The equation has complex roots")
        return None
    except ZeroDivisionError:
        print("Zero Division")

# Function to plot the roots
def PLOT_QUADRATIC(a, b, c):
    roots = QUADRATIC_EQN(a, b, c)
    if roots:
        x_values = roots
        y_values = [0, 0] 

     
        plt.scatter(x_values, y_values, color='red')


        plt.title('Roots of the Quadratic Equation')
        plt.xlabel('x')
        plt.ylabel('y')

        x = [i for i in range(int(min(x_values)) - 1, int(max(x_values)) + 2)]
        y = [a*(i**2) + b*i + c for i in x]
        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

        # Show the plot with a legend
        plt.legend()
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.show()
    else:
        print("No real roots to plot")
