Aula 13 Estrutura de repetição "for"

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer
primeiro o “for”, que é uma estrutura versátil e simples de entender. 

Por exemplo:
for c in range(0, 4):
print(c)
print(‘Acabou’)

for c in xrange(1,10):
	pass

Exemplo:
laço c no intervalo(1, 10)
	passo
pega

laço c no intervalo(1, 10)
	passo
	pula
passo
pega

(Com buracos no caminho)
for x in range(1,10):
	pass
	jump
pass
pick up

(Com moeda no caminho)
for x in xrange(1,10):
	if coin:
		pega
	passo
	pula
passo
pega

{Repetir 10x}
for x in xrange(0,10):
	print('Oi!')
print('FIM!!!')

{Contagem de 1 a 10}
for x in xrange(1,11):
	print(x)

{Contagem regressiva 1 para 10} / {Contagem regressiva 10 para 1}
# 1 até 10
from time import sleep
for x in xrange(1, 11):
	sleep(1.2)
	print(x)
print('LANÇAR!!!')

# 10 até 1
from time import sleep
for x in xrange(10, 0, -1):
	sleep(1.2)
	print(x)
print('APOLLO 11 EM LANÇAMENTO!')

n = int(input('Digite um número: '))
rr = n + 1
for x in xrange(1, rr):
	print(x)
print('Acabou!')

i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for x in xrange(i, f+1, p):
	print(x)

s = 0
for x in xrange(1, 4):
	n = int(input('Digite um valor: '))
	s += n
print('A soma de todos os valores é: {}.'.format(s))
.
.
.
.
.
.
.
.
.
[EXEMPLO DE TABUADA]
n = int(input('Numerador: '))
ml = int(input('Multiplicador: '))
r = n * ml
print('Resultado: {}'.format(r))

select = int(input('Escolha o número: '))
aux = 0
print('-'*18)
print('Tabuada de {}'.format(select))
print('-'*18)

while(aux <= 10):
	print('{0} X {1} = {2}'.format(aux, select, (aux * select)))
	aux = aux + 1
-----------------------------------------------------------------------