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

n_exp = 100
n_tes = 1000
p = np.array([0.10,0.12]).reshape(2,1,1)
sample = rng.binomial(1,p,size=(len(p),n_exp,n_tes))
de = np.mean(sample,axis=2)
data = de[1]-de[0]

fig,ax = plt.subplots()
ax.hist(data,bins=50)
ax.axvline(0,linestyle='--')
plt.show()

print("time -",time.perf_counter() - start)
