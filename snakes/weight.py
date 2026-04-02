import time
import numpy as np
import pandas as pd
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

sn_wei = pd.read_csv("snake_we.csv", encoding="cp1251", sep=";", index_col=0)
sn_wei = sn_wei.loc[sn_wei.index.notna()]
df = sn_wei.iloc[:,1:]
df = df.replace(r"[^\d.]", "", regex=True)
df = df.apply(pd.to_numeric, errors="coerce")
sn_wei[sn_wei.columns[1:]] = df
sn_wei.T.plot()
plt.show()
print(sn_wei)

print("time :",time.perf_counter() - start)
