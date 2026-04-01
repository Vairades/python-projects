def least_dif(a,b,c):
    """Возвращает наименьшее расстояние между тремя числами"""
    return min(abs(a-b),abs(b-c),abs(c-a))
#print(least_dif(1,2,8), least_dif(-1,3,9))
print(round(1.55555,2))
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

#print(
    #call(mult_by_five, 1),
    #squared_call(mult_by_five, 1), 
    #sep='\n', # '\n' is the newline character - it starts a new line
#)
def mod_5(a):
    return a%5
print('максимум по мод 5 из 1,2 и 6',max(1,6,2,key=mod_5),sep=' - ')
print('верно ли что 1=3?','\n',1==2)
print(abs(3+4j))
x = 0.125
print(x.as_integer_ratio(),' - дробь')
num, den = x.as_integer_ratio()
print(num,' - числитель\n',
      den,' - знаменатель',
      num/den,' - отношение')
# print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
Lifs = ['a','b','c','d']
def fash_late(arriv, name):
    """Проверяет пришел ли гость после первой половины и не последний"""
    return name in arriv[-(len(arriv)//2):-1]
print (fash_late(Lifs, 'd'))
print (Lifs[-1:-1])
for i in range(2):
    print("Working, i=",i)
squares = [n**2 for n in range(5)]
print(squares)

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    i=0
    while i<len(L):
        L[i] = (L[i]>thresh)
        i = i+1
    return L
numeros = [1,2,3]
print(elementwise_greater_than([1,2,3],2))
numeros[1] = numeros[1] > 2
print(numeros)
