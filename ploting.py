import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-0.5, 2.5, 200)

X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(6, 6))

F = (1-X)**2 + 100*(Y-X**2)**2
c1 = (x-1)**3 - y + 1
c2 = x +  y - 2 

cp = plt.contourf(X, Y, F, 300)
#plt.fill_between(x, np.minimum(c1), np.minimum(c2) , color='white')
plt.colorbar(cp)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
plt.show()