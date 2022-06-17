>>> Aulas 12 Condições Aninhadas

nome = str(input('Qual o seu nome? '))
print('')
if nome == 'Wallace':
	print('Seu nome é muito bonito!!')
elif nome == 'Tony Stark' or nome == 'Thor' or nome == 'Hulk' or nome == 'Steve':
	print('Pertence aos Vingadores!')
else:
	print('Um nome comum.')
print('')
print('Tenha um bom dia, {}!'.format(nome))

-----------------------------------------------------------------------

#1
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o 'valor da casa', o 'salário' do comprador e em
'quantos anos' ele vai pagar.
-- Calcule o valor da pestação mensal, sabendo que ela não exceder 30% do
sálario ou então o empréstimo será negado.

valor = float(input('Valor da residência: '))
salario = float(input('Registre o seu salário: '))
anos = int(input('Quantos anos para pagar: '))
print('')
meses = anos * 12
prest = valor / meses
if prest > salario * 0.3:
	print('Infelizmente o empréstimo não pode ser realizado...')
else:
	print('Valor da sua prestação: R${:.2f}. Empréstimo realizado!!!'.format(prest))
-----------------------------------------------------------------------
#2
Escreva um programa que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a 'base de conversão':
- 1 para 'binário'
- 2 para 'octal'
- 3 para 'hexadecimal'

print('\nEscreva um programa que leia um número inteiro qualquer e peça para o usuário escolher'
	'a base de conversão:'
	'\n1 - para binário'
	'\n2 - para octal'
	'\n3 - para hexadecimal')
print('')
num = int(input('informe um número: '))
esc = int(input('Digite "1" para binário, "2" para octal ou "3" para hexadecimal: '))
print('')
if esc == 1:
	print('O número {} em binário fica: {}.'.format(num, bin(num)))
elif esc == 2:
	print('O número {} em octal fica: {}.'.format(num, oct(num)))
elif esc == 3:
	print('O número {} em hexadecimal fica: {}.'.format(num, hex(num)))
else:
	print('Você não escolheu nenhuma das opções.')
print('-' *20)
-----------------------------------------------------------------------
#3
Escreva um programa que leia 'dois números' inteiros e compare-os, mostrando na 
tela uma mensagem:
- O 'primeiro valor' é maior
- O 'segundo valor' é maior
- 'Não existe' valor maior, os dois são 'iguais'

num1 = int(input('Escolha o primeiro valor: '))
num2 = int(input('Escolha o segundo valor: '))
print('')
if num1 > num2:
	print('O valor {} é maior que {}.'.format(num1, num2))
elif num1 < num2:
	print('O valor {} é menor que {}.'.format(num1, num2))
elif num1 == num2:
	print('Amboms valores são iguais!')
-----------------------------------------------------------------------
#4
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo 
com sua idade:
- Se ele 'ainda vai se alistar' ao serviço militar
- Se é a 'hora de se alistar'
- Se já 'passou do tempo' do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazzo.

candidato = str(input('Nome: '))
idade = int(input('Idade: '))
ano = int(input('Ano De Nascimento: '))
print('')
if idade < 18:
	print('O candidato {} ainda vai realizar o alistamento.'.format(candidato))
elif idade == 18:
	print('O alistamento de {} deverá ser feito este ano!'.format(candidato))
else:
	print('Você passou do seu prazo de alistamento.'.format(candidato))

-----------------------------------------------------------------------
#5
Crie um programa que leia duas notas de aluno e calcule sua média, mostrando 
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 15.0: 'REPROVADO'
- Média entre 15.5 e 19.0: 'RECUPERAÇÃO'
- Média 20.0 ou superior: 'APROVADO'

aluno = str(input('Nome do Aluno(a): '))
turma = int(input('Turma: '))
print('')
print('-' *20)
nota1b = float(input('Nota do 1° Bimestre: '))
nota2b = float(input ('Nota do 2° Bimestre: '))
somamd = nota1b + nota2b
#print(somamd)
print('')
nota3b = float(input('Nota do 3° Bimestre: '))
nota4b = float(input('Nota do 4° Bimestre: '))
somamd2 = nota3b + nota4b
#print(somamd2)
print('')
mediaf = somamd + somamd2
print('A MÉDIA FINAL é: {}'.format(mediaf))
if mediaf <= 15.0:
	print('O aluno está REPROVADO!')
elif mediaf == 15.5 or mediaf <= 19.0:
	print('O aluno está em RECUPERAÇÃO!')
else:
	print('O aluno está APROVADO!')
print('-' *20)
-----------------------------------------------------------------------
#6
A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até '9 anos': MIRIM
- '14 anos': INFANTIL
- '19 anos': JUNIOR
- '20 anos': MASTER

nome = str(input('Seu nome e sobrenome: '))
aluno = int(input('Registre sua idade: '))
cat1 = 'MIRIM'
cat2 = 'INFANTIL'
cat3 = 'JUNIOR'
cat4 = 'MASTER'
print('')
print('Sua categoria é:')
print('-' *20)
if aluno == 9 or aluno <= 13:
	print('O aluno pertence à categoria {}!'.format(cat1))
elif aluno == 14 or aluno <= 18:
	print('O aluno pertence à categoria {}!'.format(cat2))
elif aluno == 19:
	print('O aluno pertence à categoria {}!'.format(cat3))
elif aluno >= 20:
	print('O aluno pertence à categoria {}!'.format(cat4))
print('-' *20)
-----------------------------------------------------------------------
#7
Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
- 'Equilátero': Todos os lados iguais
- 'Isósceles': Dois lados iguais
- 'Escaleno': Todos os lados diferentes

La = float(input('Informe o comprimento da Primeira reta: '))
Lb = float(input('Segunda reta: '))
Lc = float(input('Terceira reta: '))
print('')
if (Lb - Lc)< La <(Lb + Lc) and (La - Lc)< Lb <(La + Lc) and (La - Lb)< Lc <(La + Lb):
    if (La*Lb == Lb*Lc == La*Lc) == True:
        print('É possível formar um triangulo e ele será um triangulo Equilatero')
    elif (La*Lb==La*Lc) == True:
        print('É possivel formar um triangulo e ele será um triangulo Isosceles')
    elif (La*Lb != Lb*Lc != La*Lc) == True:
        print('É possível formar um triangulo e ele será um triangulo Escaleno')
else:
    print('Não é possível formar um triangulo com essas medidas')
-----------------------------------------------------------------------
#8
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC 
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: 'Abaixo do Peso'
- Entre 18.5 e 25: 'Peso ideal'
- 25 até 30: 'Sobrepeso'
- 30 até 40: 'Obesidade'
- Acima de 40: 'Obesidade Mórbida'

alt = float(input('Registre sua altura (m): '))
pesokg = float(input('Registre seu peso (Kg): '))
print('')
imc = pesokg / (alt * alt)
#print(imc)
print('Seu IMC é {:.2f}kg/m²'.format(imc))
# O IMC é dado em kg/m²
print('-' *20)
if imc < 18.5:
	print('Você está abaixo do peso!')
elif imc == 18.5 or imc < 25:
	print('Peso ideal!')
elif imc == 25 or imc < 30:
	print('Sobrepeso!')
elif imc == 30 or imc <= 40:
	print('Obesidade!')
else:
	print('Obesidade Mórbida!!!')
print('-' *20)
-----------------------------------------------------------------------
#9
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu 'preço normal' e 'condição de pagamento':
- À vista 'dinheiro/cheque': 10% de Desconto
- À vista no 'cartão': 5% de Desconto
- Em até '2x no cartão': Preço Normal
- 3x ou mais no cartão: 20% de Juros

print('''\n- à vista dinheiro/cheque: 10% de Desconto
	\n- à vista no cartão: 5% de Desconto
	\n- em até 2x no cartão: preço normal
	\n- 3x ou mais no cartão: 20% de juros no valor total\n
''')

preco = float(input('Informe o valor do produto: R$'))
pagamento = float(input('''Escolha entre as opções abaixo:
	'\n1- à vista dinheiro/cheque: 10% de Desconto'
	'\n2- à vista no cartão: 5% de Desconto'
	'\n3- em até 2x no cartão: preço normal'
	'\n4- 3x ou mais no cartão: 20% de juros no valor total\n
	'Método De Pagamento: '''))
if pagamento == 1:
	print('O valor do produto ficará: R${:.2f}'.format(preco - (preco * 0.1)))
elif pagamento == 2:
	print('O valor do produto ficará: R${:.2f}'.format(preco - (preco * 0.5)))
elif pagamento == 3:
	print('O valor vai continuar sendo: R${:.2f}'.format(preco))
elif pagamento == 4:
	print('O valor do produto ficará: R${:.2f}'.format(preco + (preco * 0.2)))
else:
	print('Forma inválida de pagamento!!!')
-----------------------------------------------------------------------
#10 
Crie um programa que faça o computador jogar Jokenpô com você.
Pedra = 
Papel = 
Tesoura = 
# # #

from random import choice
from time import sleep
lista = ["pedra", "papel", "tesoura"]
print('''
COMPUTADOR: Vamos jogar JOKENPÔ?!
As regras são as seguintes:
- Pedra >>> Tesoura
- Papel >>> Pedra
- Tesoura >>> Papel
''')
print('')
player = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()
print('')
print('JO')
sleep(0.50)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('')
computador = choice(lista)
vencedor = ""
print('''
Player: {}
Computador: {}'''.format(player, computador))
print('')
print('-' *20)
if (player != "pedra" and player != str("papel") and player != str('tesoura')):
	print('{} não é uma opção válida. Escolha entre: Pedra, Papel ou Tesoura.'.format(player))
elif player == computador:
	print('Empate!!!')

# Jogadas válidas

elif player == "pedra" and computador == "tesoura":
	print('''O Player venceu! 
		PEDRA >>> TESOURA.''')
elif player == "papel" and computador == "pedra":
	print('''O Player venceu!
		PAPEL >>> PEDRA.''')
elif player == "tesoura" and computador == "papel":
	print('''O Player venceu!
		TESOURA >>> PAPEL.''')
elif computador == "pedra" and player == "tesoura":
	print('''O Computador venceu! 
		PEDRA >>> TESOURA.''')
elif computador == "papel" and player == "pedra":
	print('''O Computador venceu!
		PAPEL >>> PEDRA.''')
elif computador == "tesoura" and pla == "papel":
	print('''O Computador venceu!
		TESOURA >>> PAPEL.''')
print('-' *20)
-----------------------------------------------------------------------
