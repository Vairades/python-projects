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

n = 100
sep = np.arange(0.1,1.,0.1)
sample = np.zeros((len(sep),n))
p = sep[:,None]
sample = rng.binomial(1, p, size=(len(sep), n))
reg = np.cumsum(sample,axis=1)/np.arange(1,n+1)

cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(sep)))
fig, (ax1, ax2) = plt.subplots(1, 2)
for i in range(len(sep)):
    ax1.plot(reg[i], color=colors[i])
    ax1.hlines(sep[i], 0, n, color=colors[i], linestyle='--')

    ax2.plot(abs(reg[i] - sep[i]), color=colors[i])
plt.savefig("dist")

print("time -",time.perf_counter() - start)
