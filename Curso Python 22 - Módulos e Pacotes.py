Aula 22 – Módulos e Pacotes

def fatorial(n):
    f = 1
    for c in range(1, n +1):
        f *= c
    return f

def dobro(n):
    return n *2

def triplo(n):
    return n *3


# ---
import uteis

num = int(input('Digite um valor: '))
print('')
fat = uteis.fatorial(num)
print('O fatorial de {}! é: {}.'.format(num, fat))
db = uteis.dobro(num)
print('>>> O dobro de {} é: {}.'.format(num, db)) 
tp = uteis.triplo(num)
print('>>> O triplo de {} é: {}.'.format(num, tp))
