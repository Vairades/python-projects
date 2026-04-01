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

sample = rng.choice([0,1],p=[0.8,0.2],size=(10000,1000))
me = np.mean(sample, axis=1)

fig, ax = plt.subplots()
ax.hist(me,bins=50,density=True)
plt.show()

print("time -",time.perf_counter() - start)
