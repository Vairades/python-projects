a = 1
while a < 1000:
    if (500000 - 1000*a) % (1000 - a) == 0:
        b = ((500000 - 1000*a) // (1000 - a))
        print(a*b*((a*a + b*b)**0.5))
        break
    else:
        a = a+1
