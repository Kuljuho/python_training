import numpy as np
import matplotlib.pyplot as plt

N=100

t=np.arange(0, 2*np.pi, 2*np.pi/N)
x=np.sin(2*t)
y=np.cos(t)

plt.figure(figsize=(16, 8))
data={'x': x, 'y': y, 's':40*t+1, 'c':np.random.randint(0, 50, size=x.shape)}
plt.scatter('x', 'y', s='s', c='c', data=data)
plt.xlabel('sin(2t)')
plt.ylabel('cos(t)')
plt.grid(linestyle=':')
plt.show()

names=['A', 'B', 'C']
values=[1, 10, 100]
colors=['black', 'red', 'blue']

plt.figure(figsize=(16,8))
plt.subplot(131)
plt.bar(names, values, color=colors)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.show

YT=np.reshape(y, (1, N))
X=np.reshape(x, (N, 1))
A=X+YT

plt.imshow(A, cmap='jet')
plt.colorbar()
plt.show

fig=plt.figure(figsize=(8, 8))
ax = plt.axes(projection ='3d')
px,py=np.meshgrid(t, t)
surf=ax.plot_surface(px, py, A, cmap='jet')
fig.colorbar(surf, shrink=0.5)
plt.show()