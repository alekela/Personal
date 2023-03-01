import matplotlib.pyplot as plt
import numpy as np
from random import randint, choice


def r(t, n, d, alpha):
    return alpha * np.sin(n / d * t)


plt.rc('text', usetex=True)
fig = plt.figure()

axs = [fig.add_subplot(221, projection='polar'), fig.add_subplot(222, projection='polar'),
       fig.add_subplot(223, projection='polar'), fig.add_subplot(224, projection='polar')]
plt.subplots_adjust(hspace=0.5)

for i in range(4):
    axs[i].set_rgrids(())
    axs[i].set_thetagrids(angles=(0, 45, 90, 135, 180, 225, 270, 315))
    # бессмысленно, потому что по умолчанию так, но просто показываю, что умею настраивать сетку

alpha = randint(1, 10)
ns = [randint(10, 60), choice([1, 2, 3, 5, 6, 7]), 5, randint(10, 40)]
ds = [randint(4, 10), 4, choice([1, 2, 3, 4, 6, 7]), randint(4, 9)]
t = np.linspace(0, 2 * np.pi, 300)

for i in range(4):
    axs[i].plot(t, r(t, ns[i], ds[i], alpha))
    axs[i].set_title(f"$r(t) = {alpha}*sin(\\frac{{{ns[i]}}}{{{ds[i]}}}t)$")

plt.savefig('2_1.pdf')
plt.show()
