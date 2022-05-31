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
num = int(input('Digite um valor: '))
fat = fatorial(num)
print('O fatorial de {}! é: {}.'.format(num, fat))
print('>>> O dobro de {} é: {}.'.format(num, dobro(num))) 
print('>>> O triplo de {} é: {}.'.format(num, triplo(num)))
