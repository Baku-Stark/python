Aula 14 Estrutura de repetição "while"


Nessa aula, vamos continuar a estudar os laços e vamos aprender a 
usar a estrutura de repetição while no Python. Por exemplo:

c=1 while c !=10:

print(c)

c+=1

print(‘Acabou’)
-----------------------------------------------------------------------

while enquanto não maça:
	if bloco:
		passo
	if espaço:
		pula
	if coin:
		pega
pega #maçã

c = 1
while c < 10:
	print(c)
	c += 1
print('Acabou!')

n = 1
while n != 0:
	n = int(input('Digite um número: '))
print('Finalizou!')

r = 'S'
while r == 'S':
	print('-=' *5)
	n = int(input('Digite um número: '))
	r = str(input('Deseja continuar [S/N]: ')).upper()
	print('-=' *5)
	print('')
print('Sessão encerrada!')

n = 1
par = impar = 0
while n != 0 :
	n = int(input('Digite um valor: '))
	if n != 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

# Outro Modelo
n = 1
par = impar = 0
while n != 0 :
	n = int(input('Digite um valor: '))
	if n % 2 == 0:
		par += 1
	else:
		impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
