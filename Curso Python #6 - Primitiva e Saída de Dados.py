>>> Primitiva e Saída de Dados
n = input('Digite um valor:')
print(type(n))

	# Passo --- 1
n1 = input('Digite um valor:')
print(type(n1))

n1 = input('Digite um número:')
n2 = input('Digite um número:')

sr = int(n1)+int(n2)

	print('A soma vale', sr)
	print('A soma entre', n1, 'e', n2, 'vale', sr)
	--- print('A soma vale{}'.format(sr))

--------------------------------------------------------
	n = input('Digite um número')

n = int(input('Digite um número:')) 
n = float(input('Digite um número:'))
n = str(input('Digite um número'))
n = bool(input('Digite um número'))

print(n)
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())

