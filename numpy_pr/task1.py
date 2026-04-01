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

sample = rng.integers(0,2,size=(50,1000))
me = np.cumsum(sample,axis=1) / np.arange(1,len(sample[0])+1)

fig, ax = plt.subplots()
ax.plot(me.T)
plt.show()

print("time -",time.perf_counter() - start)
