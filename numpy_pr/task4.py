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

#средняя ошибка по 100 экспериментам
sep = np.arange(0.1,1.,0.1)
p = sep[:,None,None]
n = (len(sep),100,100)
data = rng.binomial(1,p,size=n)
me = abs(np.cumsum(data,axis=2)/np.arange(1,data.shape[2]+1)-p)
me = np.mean(me,axis=1)

cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(sep)))
fig, ax = plt.subplots()
for i in range(len(sep)):
    ax.plot(me[i], color=colors[i])
plt.show()

print("time :",time.perf_counter() - start)
