Aula 17 – Listas (Parte 1)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma 
mesma estrutura, acessíveis por chaves individuais.
-----------------------------------------------------------------------

num = ['1', '2', '9', '4']
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)

valores = []
valores.append (5)
valores.append (9)
valores.append (4)
for c, v in enumerate(valores):
	print('Na posição {} encontrei o valor {}'.format(c, v))
print('Cheguei ao fim!')

valores = []
for cont in range(0, 5):
	valores.append(int(input('>>> Digite um valor \nr: ')))
for c, v in enumerate(valores):
	print('Na posição {} encontrei o valor {}'.format(c, v))

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print('Lista A: {}'.format(a))
print('Lista B: {}'.format(b))