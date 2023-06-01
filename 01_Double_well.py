import numpy as np
import matplotlib.pyplot as plt
def double_well_potential(x):
    return (x**2 - 1)**2

x = np.linspace(-2, 2, 100)

potential = double_well_potential(x)

plt.plot(x, potential)
plt.xlabel('x')
plt.ylabel('Potential Energy')
plt.title('Double Well Potential')
plt.grid(True)
plt.show()
