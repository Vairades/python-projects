import numpy as np
a = np.arange(6)
print(a.reshape(3,2),a.reshape(3,2,1),a.reshape(2,3,1),a.reshape(2,1,3),a.reshape(1,3,2),sep='\n,\n')

a2 = a[np.newaxis, :]
print(a2)
print(a.reshape(3,2)[np.newaxis, :])
print(a[:, np.newaxis])
print(a.reshape(3,2)[:, np.newaxis, :].shape)
print(np.expand_dims(a, axis=1).shape)
a = np.arange(9).reshape(3,3)
print(np.nonzero(a<5))
print(a<5)
print(a[a<5])
print(np.nonzero(a))
