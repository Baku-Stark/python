Aula 18 – Listas (Parte 2)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
acessíveis por chaves individuais.

Exemplo
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) --> Pedro
print(pessoas[1][1]) --> 19
print(pessoas[2][0]) --> João
print(pessoas[1]) --> ['Maria', 19]

Prática
test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)


-> Print [nome]
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
for p in pessoas:
	print(p[0])
-> Print [idade]
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
for p in pessoas:
	print(p[1])

pessoas = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 3):
	dados.append(str(input('Nome do usuário \nr: ')))
	print('')
	dados.append(int(input('Idade \nr: ')))
	print('-=' *15)
	pessoas.append(dados[:])
	dados.clear()
print('')
for p in pessoas:
	if [1] >= 21:
		print('{} é maior de idade!'.format(p[0]))
		totmaior += 1
	else:
		print('{} é menor de idade!'.format(p[0]))
		totmenor += 1
print('''Temos {} maiores de idade
Temos {} menores de idade.'''.format(totmaior, totmenor))
-----------------------------------------------------------------------
