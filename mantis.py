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

def mant(p,t,L,U):
    """Выводит множество чисел с плавоющей точкой F по параметрам p,t,L,U"""
    divisitors = p**np.arange(1,t+1).reshape(t,1) #строим знаменатели мантиссы
    d = (np.zeros((t,p)) + np.arange(0,p))/divisitors #строим слагаемые мантиссы
    m = d[0,1:]
    for i in range(1,t):
        m = (m[:,None] + d[i,None]).ravel() #мантисса через broadcasting
    alp = np.arange(L,U+1,dtype=float) #степени из интервала показателей
    F = p**alp[:,None] * m[None] #умножаем мантиссу на p^alp
    F = np.hstack((F,-F)).ravel() #добавляем отрицательные числа
    F = np.hstack((F,0)) #добавляем 0
    return F

p,t,L,U = 2,3,-1,2
y = np.array([23/32,1/8,4,1/2+3/4,3/8+5/4,3+7/2,7/16-3/8,(1/4)*(5/16)]) #числа которые надо округлить
F = mant(p,t,L,U)
epsilon = (p**(1-t))/2 #машинная точность

cmap = plt.get_cmap('viridis') #цыета
colors = cmap(np.linspace(0, 1, len(y)))

flt, ax = plt.subplots(figsize=(16,3))
ax.scatter(F,np.zeros_like(F),s=50) #рисует множество F
for i in range(len(y)):
    ax.scatter(y[i],0,c=colors[i],s=7,label=f"y={y[i]}") #рисует числа
ax.vlines(x=y*(1+epsilon),colors=colors,ymin=-0.1,ymax=0.1)
ax.vlines(x=y*(1-epsilon),colors=colors,ymin=-0.1,ymax=0.1)
ax.set_title(f"p={p}, t={t}, [L,U]=[{L},{U}]")
ax.legend()
plt.show()

print("time :",time.perf_counter() - start)
