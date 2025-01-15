def fibonaci(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibonaci(n-2)+fibonaci(n-1)
print(fibonaci(108))

def funcion_suma(n,m):
    return n+m
print(funcion_suma(14,27))