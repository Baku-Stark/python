Aula 15 – Interrompendo repetições while

Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a 
favor das nossas estratégias de código. É muito importante saber usar o break no Python, 
já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

-----------------------------------------------------------------------

while enquanto não maça:
	if bloco:
		passo
	if espaço:
		pula
	if coin:
		pega
pega #maçã

while True:
	if bloco:
		passo
	if espaço:
		pula
	if coin:
		pega
	if trofeu:
		pega
		break
pega #maçã
-----------------------------------------------------------------------

cont = 1
while cont <= 10:
	print(cont),
	print('...'),
	cont += 1
print('Acabou !!!')

cont = 1
while True:
	print(cont),
	print('...'),
	cont += 1
print('Acabou !!!')

n = cont = 0
while cont < 5:
	n = int(input('Digite um número: '))
	cont += 1


n = 0
while n != 999:
	n = int(input('Digite um número: '))


n = s = 0
while n != 999:
	n = int(input('Digite um número: '))
	s += n
print('A soma vale {}.'.format(s - 999))

n = s = 0
while True:
	n = int(input('Digite um número: '))
	if n == 999:
		break
	s += n
print('A soma vale {}.'.format(s))


.
.
.
.
.
cont = 1
while cont <= 10:
	print(cont, '...'),
	cont += 1
print('Acabou !!!')
-----------------------------------------------------------------------