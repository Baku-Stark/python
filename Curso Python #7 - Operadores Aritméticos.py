>>> Operadores Aritméticos

n1 = int(input('Digite um valor´:'))
n2 = int(input('Digite um valor´:'))

soma = n1 + n2
print ('O resultado é: {}'.format(soma))

> Soma, Multiplicação, Divisão, Divisão inteira e Potência

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
divint = n1 // n2
pot = n1 ** n2 

print('O resultado é: {}', '{}', '{}', '{}'.format(soma, sub, multi, div))
print('O resultado é: {}', '{}'.format(divint, pot))

# Desafio 1 - Mostrar o antecessor e sucessor de um número
n1 = int(input('Número:'))
ant = n1 - 1
suc = n1 + 1

print('antecessor: {}'.format(ant))
print('sucessor:{}'.format(suc))

# Desafio 2 - Mostrar o Dobro, Triplo e Raiz Quadrada
n1 = int(input('Número:'))
rq = n1 **(1/2)
dou = n1 *2
tri = n1 *3

print('Raiz Quadrada: {}'.format(rq))
print('Dobro: {}'.format(dou))
print('Triplo: {}'.format(tri))

# Desafio 3 - Ler as notas e calcular a nota. Depois mostrar a média
b1 = int(input('Nota do 1° Bimestre:'))
b2 = int(input('Nota do 2° Bimestre:'))

med = (b1 + b2)/2
print('A média é: {}'.format(med))

# Desafio 4 - Escrever um valor em metros, convertê-los para centimetros e milímetros
m = int(input('Metro:'))
cm = m *100
ml = m *1000

print('Centímetro: {}'.format(cm))
print('Milímetro: {}'.format(ml))

# Desafio 5 - Ler um número e mostrar toda a sua tabuada
n = int(input('Numerador:'))
ml = int(input('Multiplicador:'))
r = n * ml
print('Resultado: {}'.format(r))

select = int(input('Escolha o número:'))
aux = 0
print('-'*18)
print('Tabuada de {}'.format(select))
print('-'*18)

while(aux <= 10):
	print('{0} X {1} = {2}'.format(aux, select, (aux * select)))
	aux = aux + 1
	
# Desafio 6 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar (Considera: US$1,00 = R$3.27)
print('-'*18)
print('Quantia na carteira')
print('R$ 6,54')
print('-'*18)

compra = int(input('Quantia em Dólar: '))
res = 6.54 - float(compra)
print('Seu troco é: {}'.format(res))

# Desafio 7 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2
alt = float(input('Altura da parede:'))
larg = float(input('Largura da parede:'))
area = alt * larg
tinta = area /2

print('A área da parede é {} e precisará de {}L de tinta'.format(area, tinta))

# Desafio 8 - Faça um algoritmo que leia o preço de uma produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Valor do produto:'))
desconto = produto *5
desconto_produto = produto - desconto
print('O valor total com desconto de 5% é: {}', 'você economizou: {}'.format(desconto_produto, desconto))

# Desafio 9 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto
salario = float(input('Atual sálari:'))
aumento = salario *0.15
sal_aumento = salario + aumento
print('Salário após o aumento é {} e seu aumentou foi de {}'.format(sal_aumento, aumento))