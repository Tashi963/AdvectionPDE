## Finite Difference

# 1. Diffusion (Heat Conduction) in 1D

import numpy as np
import matplotlib.pyplot as plt


# 1. Temperature Bathed at both ends 


x = np.linspace(0, 1, 101)
u = np.zeros(101)

u[0], u[100] = 1, 1

for time in range (100):
    u[1:-1] += 0.25 * (u[2:] - 2*u[1:-1] + u[:-2])

plt.plot(x, u)
plt.show()


"""
for i in range(1, 100):
    u[i] += (u[i+1] - 2*u[i] + u[i-1])/4 
    
This code can be reduced appreciably by NumPy slicing:

u[1:-1] += 0.25 * (u[2:] - 2*u[1:-1] + u[:-2])


Also 

u = np.zeros(101)
u[50] = 1

can be reduced to

u = np.exp(-(x - 0.5) ** 2 / 0.001)

"""



# 2. Uniformly Heated Rod

T0, L = 1, 1
x = np.linspace(0, L, 101)

u = T0 * np.ones(101)
u[0], u[100] = 0, 0 


for time in range(100):
    u[1:-1] += 0.25 * (u[2:] - 2*u[1:-1] + u[:-2])

t = 1.0 / 300

f = lambda m: 2.0 / (2*m - 1) * T0 / np.pi * np.exp(-((2*m - 1)* np.pi/L) ** 2 * t) * np.sin((2*m - 1) * np.pi * x / L)

exact = sum([f(m) for m in range(1, 20)])

plt.plot(x, u, 'o', x, exact, lw = 3)
plt.show()



# 3. Insulated Rod

x1 = np.linspace(0, 1, 101)
x2 = np.linspace(1, 2, 100)

x = np.concatenate([x1, x2])
u = np.concatenate([100*x1, 100*np.ones(100)])
  
u[0], u[200] = 0, 100

for time in range(100):
    u[1:-1] += 0.25 * (u[2:] - 2*u[1:-1] + u[:-2])

t = 1.0 / 300
k = 1.14 * 10**(-4)

f = lambda n: 50*x + (400 / n * np.pi**2 * np.sin((n*np.pi) / 2) * np.exp(- 0.25*n**2*np.pi**2*k*t)*np.sin(0.5*n*np.pi*x))


exact = sum([f(n) for n in range(1, 20)])

plt.plot(x, u, 'o', x, exact, lw = 3)
plt.show()




