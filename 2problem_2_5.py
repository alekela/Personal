import numpy as np
import matplotlib.pyplot as plt
from random import random, choice, randint
import scipy.constants as sc


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def H(x, y, x0, y0, I):
    if x == x0 and y == y0:
        return ("Wire", sgn(I))
    return sc.mu_0 * I / 2 / sc.pi / ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5


plt.rc('text', usetex=True)
step = 100
xgrid = np.linspace(0, 1, step + 1)
ygrid = np.linspace(0, 1, step + 1)

amperages = []
coords = []
for i in range(3):
    t1 = randint(1, step - 1)
    t2 = randint(1, step - 1)
    coords.append((t1, t2))
    amperages.append((t1, t2, choice([-1, 1]) * (1000 + int(random() * 2000))))
print(amperages)

data_for_map = [[0 for _ in range(step + 1)] for _ in range(step + 1)]
for y in range(step + 1):
    for x in range(step + 1):
        if (x, y) not in coords:
            data_for_map[x][y] = sum(H(xgrid[x], ygrid[y], xgrid[I[0]], ygrid[I[1]], I[2]) for I in amperages)

limits = []
for x, y in coords:
    data_for_map[x][y] = (data_for_map[x - 1][y] + data_for_map[x][y + 1] + data_for_map[x][y - 1] +
                          data_for_map[x + 1][y]) / 4
    limits.append(abs(data_for_map[x][y]))

ptr = plt.contourf(xgrid, ygrid, data_for_map, cmap=plt.cm.cividis, levels=50, extend='both')

plt.colorbar(ptr, ticks=[i for i in np.linspace(-max(limits), max(limits), 10)])

plt.xlabel('$x$', fontsize=18)
plt.ylabel('$y$', fontsize=18)
plt.title('$H(x,y)$', fontsize=22)
plt.show()
