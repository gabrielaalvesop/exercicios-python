def fatorial(numero, show=False):
    fatorial=1
    for c in range(numero,0,-1):
        if show:
            print(c, end=' ')
            if c>1:
                print("x", end=' ')
            else:
                print("=", end=' ')
        fatorial *= c
    return fatorial


print(fatorial(5, show=True))
