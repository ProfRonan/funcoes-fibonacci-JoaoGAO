def fibonacci(n):
    if n<0:
        raise ValueError("Não existe fibonacci com n negativo")
    if type(n) != int:
        raise ValueError("Só serve com numeros inteiros")
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
