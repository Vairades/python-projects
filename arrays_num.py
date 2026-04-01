import numpy as np

E = np.array([0,1,2,3])
a = np.array([])
print(a,a.shape,a.ndim,a.size)
a = np.array([1])
print(a,a.shape,a.ndim,a.size)
b = np.array([1,2])
print(b,b.shape,b.ndim,b.size)
c = np.array([[]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[1]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[[]]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[[1]]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[1,2]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[[],[]]])
print(c,c.shape,c.ndim,c.size)
c = np.array([[[1],[2]]])
print(c,c.shape,c.ndim,c.size)
d = np.array([[],[]])
print(d,d.shape,d.ndim,d.size)
d = np.array([[1],[2]])
print(d,d.shape,d.ndim,d.size)
f = np.array([[1,2],[3,4]])
print(f,f.shape,f.ndim,f.size)
f = np.array([[[1],[2]],[[3],[4]]])
print(f,f.shape,f.ndim,f.size)
h = np.array([[1,2],[3,4],[5,6]])
print(h,h.shape,h.ndim)
print(f[0,1])

e = E[1:-1]
print(E,e)
E[1:-1] = [10,20]
print(E,e) #e поменялся тк E поменялся
e = [7,8]
print(E,e) #e поменялся, но E нет
E[1:-1] = [5,6]
print(E,e)

