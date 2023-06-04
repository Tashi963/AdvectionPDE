# Approximation of exponential Function e^x

# Small Essentials

import numpy as np
print(np.pi)

import matplotlib.pyplot as plt
plt.plot(range(10))



# Let us consider a few ways of building a numerical sequence. Assume ∆x = f(k) , where k is an integer number defined in k = 1,2,3,...,9.

# 1. Create a Python list in a loop and then transform it into a NumPy array
delta_list = []

for k in range(1, 10):
    delta_list.append(2**(-k))

delta = np.array(delta_list)
print(delta)


# 2. Create Python List using list comprehension and the convert it to a NumPy array
delta_list = [2**(-k) for k in range(1,10)]

delta = np.array(delta_list)
print(delta)


# 3. Create empty NumPy array and then fill it with values in a loop
delta = np.zeros(9)

for i in range(len(delta)):
    delta[i] = 2**(-i-1)



# We are set to build R3
delta = np.zeros(9)

for i in range(len(delta)):
    delta[i] = 2**(-i-1)

R3 = np.exp(delta) - (1 + delta + delta**2 / 2)
print(R3)

slope = delta**3
print(slope)


# As we have built the set of numerical data, we are ready to visualize it.

fig, ax = plt.subplots()

# Create a plot with log scaling. Pass x-data as the first argument,
# y-data as the second argument, other arguments are optional.
# '*' means that we want a dot plot with stars as markers.
# Label argument defines the description for the data, which will be 
# displayed in the legend.

ax.loglog(delta, R3, '*', label='$R_3$')

# We plot delta^3 with the same log scaling to show the R3 is of 
# order delta^3. See that you can configure the color of dots and
# lines you plot with the color argument.

# This is one way to set a color of a curve by simply passing the name
# of a color to the function. But this way is limited to only 8 colors.
# More info: https://matplotlib.org/3.1.1/tutorials/colors/colors.html

ax.loglog(delta, slope, color = 'blue', label = r'$\Delat^{3}$')

# We set labels of x-axis and y-axis.
ax.set_xlabel(r'$\Delta x$')
ax.set_ylabel('$R_3$')

# We set the title, which in this case is only related to the subplot 
# referred to ax, but as we have only 1 subplot, it is then related
# to the whole figure and can be used instead of 'fig.suptitle'.

ax.set_title('Accuracy')

# Enable automatic detection of elements to be shown in legend.
ax.legend()

# Save figure. Default format is png.
# dpi defines the resolution in dots per inch.
fig.savefig('../figures/taylorSlope', dpi=300)