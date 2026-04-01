import time
import numpy as np
import matplotlib.pyplot as plt
start = time.perf_counter()
rng = np.random.default_rng()
plt.style.use("dark_background")

plt.rcParams.update({
    # фон
    "figure.facecolor": "#0F1419",
    "axes.facecolor": "#0F1419",

    # текст
    "text.color": "#C8F7E5",
    "axes.labelcolor": "#C8F7E5",
    "xtick.color": "#C8F7E5",
    "ytick.color": "#C8F7E5",

    # сетка
    "grid.color": "#444444",
    "grid.linestyle": "--",
    "grid.alpha": 0.4,

    # линии
    "lines.linewidth": 2.2,

    # рамки
    "axes.edgecolor": "#767676",
})

x = np.linspace(1,100)
fig, (ax1, ax2) = plt.subplots(1,2)
num = rng.integers(2,size=100)
avg = np.array([num[:i].mean() for i in range(1,len(num))])
ax1.plot(avg,'o')
ax1.axhline(0.5)
ax2.plot(abs(avg - 0.5))
ax2.plot(x,1/(x**0.5))

plt.show()
print("time -",time.perf_counter() - start)
