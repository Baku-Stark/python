>>> Curso Python #10 - Condições (Parte 1)

____________________________________________________________________
Exemplos básicos (Estrutura Condicional): 

se cara.esquerda()          if carro.esquerda():
	bloco_V_					bloco True

senão                       else:
	bloco_F_					bloco False
____________________________________________________________________

tempo = int(input('Quantos tem seu carro?'))
if tempo<=3:
	print('Carro Novo')
else:
	print('Carro Velho')
print('-- FIM ! --')

tempo = int(input('Quantos tem seu carro?'))
print('Carro Novo'if tempo<=3 else'Carro Velho')
print('-- FIM ! --')
____________________________________________________________________

nome = str(input('Qual o seu nome?'))
if nome == 'Wallace':
	print('Que nome bonito!')
else:
	print('Bom dia, {}! O seu nome é tão feio...'.format(nome))

n1 = float(input('Primeiro Bimestre:'))
n2 = float(input('Segundo Bimestre:'))
md = n1 + n2 
print('Sua média foi: {}'.format(md))
print('-' *20)
if md>=10:
	print('Aprovado!!! Boas Festas!!!')
	print('O aluno está pronto para seguir para o próximo ano!')
else:
	print('Recuperação :(')
print('-' *20)
____________________________________________________________________

# Desafio 01
* Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.
O programa deverá escrever na se o usuário venceu ou perdeu.
from random import randint
nrand = randint(0, 5)
print('')
print('Vou sortear um número de 0 a 5')
print('')
user = int(input('Escolha um número de 0 a 5:'))

if user == nrand:
	print('Parabéns! Você acertou!')
else:
	print('Sinto muito, mas o resultado era {}'.format(nrand))

# Desafio 02 
* Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado,
-- 'A multa vai custar R$7,00 por cada KM acima do limite' --
vel = int(input('Registre a velocidade:'))
print('')
multa = vel - 80 
#print('Km acima do limite: {}'.format(multa))
pagamento = multa * 7
print('-' *20)
if vel>=80:
	print('Sua multa é de: R${},00'.format(pagamento))
else:
	print('Nenhuma multa foi prevista!')
print('-' *20)

# Desafio 03
* Crie um programa que um número inteiro e mostre na tela se ele é PAR ou IMPAR.
num = int(input('Digite um número inteiro:'))
num1 = num % 2
print('')
print('-' *20)
if num1 == 0:
	print('Seu número é PAR.')
else:
	print('Seu número é IMPAR')
print('-' *20)

# Desafio 04
* Desenvolva um programa que pergunta a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km
e R$0,45 para viagens mais longas.
dis = int(input('Distância da sua viagem em KM:'))
if dis<=200:
	resultado = dis * float(0.50)
	print('Sua passagem (Curta) é: R${}0'.format(resultado))
else:
	resultadoc = dis * float(0.45)
	print('Sua passagem (Longa) é: R${}0'.format(resultadoc))

# Desafio 05
* Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
num = int(input('Escolha o ano:'))
num1 = num % 4
if num1 == 0:
	print('Seu ano é bissexto.')
else:
	print('Seu ano não é bissexto.')

# Desafio 06
* Faça um programa que leia três números e mostre qual é o MAIOR e o MENOR.
num1 = int(input('Escolha o número:'))
print('')
num2 = int(input('Escolha o número:'))
print('')
num3 = int(input('Escolha o número:'))
print('')
print('-' *20)
if num1 > num3 > num2:
	print('{} é maior e {} é o menor'.format(num1, num2))
elif num2 > num3 > num1:
	print('{} é maior e {} é o menor'.format(num2, num1))
elif num1 > num2 > num3:
	print('{} é maior e {} é o menor'.format(num1, num3))
elif num2 > num1 > num3:
	print('{} é maior e {} é o menor'.format(num2, num3))
elif num3 > num2 > num1:
	print('{} é maior e {} é o menor'.format(num3, num1))
elif num3 > num1 > num2:
	print('{} é maior e {} é o menor'.format(num3, num2))
print('-' *20)

# Desafio 07
* Escreva um programa que pergunte o sálario de um funcionário e calcule o valor
do seu aumento.
- Para salários superiores a R$1.250.00, calcule um aumento de 10%. # *1.1
- Para inferiores ou iguais, o aumeno é de 15%. # *1.15
salario = float(input('Digite o sálario:'))
print('')
print('-' *20)
if salario > 1250:
	nsalario = salario *1.1
	print('Seu novo salário é: {:.2f}'.format(nsalario))
else:
	nsalario2 = salario *1.15
	print('Seu novo salário é: {:.2f}'.format(nsalario2))
print('-' *20)

# Desafio 08
* Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas pode ou não formar um triângulo.
reta1 = float(input('Reta 1:'))
reta2 = float(input('Reta 2:'))
reta3 = float(input('Reta 3:'))
g = reta1 + reta2
p = reta1 - reta3
print('')
print('-' *20)
if g > reta3 > abs(p):
	print('As retas podem formar um triângulo!')
else:
	print('As retas NÃO podem formar um triângulo!')
print('-' *20)
