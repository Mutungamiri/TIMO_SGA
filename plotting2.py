import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects

fig, ax = plt.subplots(figsize=(6, 6))#   w w w .  de  mo 2  s  . co  m

nx = 101
ny = 105

# Set up survey vectors
xvec = np.linspace(-1.5, 1.5, nx)
yvec = np.linspace(-1.5, 1.5, ny)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)

# Evaluate some stuff to plot
obj = (1-x1)**2 + 100*(x2-x1**2)**2
g1 = -(3*x1 + x2 - 5.5)


cntr = ax.contourf(x1, x2, obj)
ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)

cg1 = ax.contour(x1, x2, g1)
plt.setp(cg1.collections,
         path_effects=[patheffects.withTickedStroke(angle=135)])



plt.show()