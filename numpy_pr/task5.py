import time
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()
start = time.perf_counter()

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

print(rng.binomial(10,0.5,10))

print("time :",time.perf_counter() - start)
