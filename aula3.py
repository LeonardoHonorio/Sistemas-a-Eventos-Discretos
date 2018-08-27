import numpy
v = []

def nfatorial(n):
    if n==1:
        print('final 1.. retornando')
        return 1
    else:
        print('passando %d ' % n)
        parcial = nfatorial(n-1)
        print('acumulado %d multiplicando por %d' % (parcial,n))
        v.append(n)
        return n*parcial

    return 0

print('resultado = %d' % nfatorial(5))

