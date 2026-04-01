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

cash = 100
n_exp = 100
n_time = cash**2
dat = rng.choice([-1,1],p=[0.5,0.5],size=(n_exp,n_time))
dat = np.cumsum(dat,axis=1) + cash
dat[dat < 0] = 0
dt = dat.T
print(f"вероятность не обнулиться={np.count_nonzero(dt[-1])/n_exp} время={n_time}")

fig, ax = plt.subplots()
ax.plot(dat.T)
plt.show()

print("time :",time.perf_counter() - start)
