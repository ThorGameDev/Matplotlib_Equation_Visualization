import matplotlib.pyplot as plt
import numpy as np

#Constant definition
e=2.71828

# Create the axis
ax = plt.axes(projection='3d')

# Inputs
x = np.arange(-10,10,0.1)

# e^ix outputs
output_eix=[e**(1j*theta) for theta in x]
output_eix_r=[n.real for n in output_eix]
output_eix_i=[n.imag for n in output_eix]
ax.plot(x, output_eix_r, output_eix_i)

# (cosx, sinx)
output_sinx=[np.sin(theta) for theta in x]
output_cosx=[np.cos(theta) for theta in x]
ax.plot(x, output_cosx, output_sinx)

ax.set_title("e^ix")
plt.gca().set_aspect('equal')
plt.show()
