import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpch

n=np.linspace(0,199,200)    

#Function inputs the value of n to the equation given.
def x(n): 
#Converting string input to an integer
    e=eval(x1)  
    return e 

#Inputing the Equation
    
print("\nExample Input: np.sin(np.pi*3*n/100)")
x1=(input("Input your Equation x(n):"))   
 
for i in range(0,200):
    if i==0:
        y=(-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2))
    elif i==199:
        y=(1.5*x(n))-(2*x(n-1))+(0.5*x(n-2))
    else:
        y= (0.5*x(n+1))-(0.5*x(n-1))
         
#Plot specifications
plt.figure(figsize=(10,7))
plt.plot(x(n),color="b")
plt.plot(y,color="r")
plt.suptitle('f(x(n))')
plt.xlabel('n in range of (0,199)')
#Legend
b=mpch.Patch(color='red', label='y(n) data')
g=mpch.Patch(color='blue', label='x(n) data')
plt.legend(handles=[g,b])

plt.show


   
    
    



    