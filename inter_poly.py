import numpy as np

def det2minor(m,i0=0,i1=1,j0=0,j1=1):
    """Считает 2 на 2 минор"""
    return m[i0][j0]*m[i1][j1]-m[i0][j1]*m[i1][j0]

def det3minor(m,i0=0,i1=1,i2=2,j0=0,j1=1,j2=2):
    """Считает 3 на 3 минор"""
    return m[i0][j0]*det2minor(m,i1,i2,j1,j2)-m[i0][j1]*det2minor(m,i1,i2,j0,j2)+m[i0][j2]*det2minor(m,i1,i2,j0,j1)

def interpol(dots):
    """Интерполирует три точки (пока только 3) многочленом"""
    x = []
    y = []
    ans = []
    for i in range(len(dots)):
        x.append(dots[i][0])
        y.append(dots[i][1])
    line = []
    matrix = []
    for i in range(len(dots)):
        for j in range(len(dots)):
            line.append(x[i]**j)
        matrix.append(line)
        line = []
    det = det3minor(matrix)
    for j in range(len(dots)):
        subm = np.array(matrix)
        for i in range(len(dots)):
            subm[i][j] = y[i]
        ans.append(float(det3minor(subm)/det))
    print('Результат: f(x)=',sep='',end='')
    for i in range(len(ans)):
        if i == 0:
            print(ans[i],sep='',end='')
        elif i!=0 and ans[i]>0:
            print('+',ans[i],'x^',i,sep='',end='')
        elif i!=0 and ans[i]<0:
            print(ans[i],'x^',i,sep='',end='')
    print()
    return ans

dots = [(0,1),(1,2),(2,0)]
interpol(dots)
interpol([(0,1),(1,1),(2,3)])
