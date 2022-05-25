Aula 20 – Funções (Parte 1)

def mostraLinha():
	print('------------------------------')


mostraLinha()
print('     SISTEMA DE ALUNOS     ')
mostraLinha()
print('')
mostraLinha()
print('     CADASTRO DE ALUNOS     ')
mostraLinha()
print('')
mostraLinha()
print('     SISTEMA ESCOLAR     ')
mostraLinha()
--------------------------------------------------------

def mensagem(msg):
	print('------------------------------')
	print(msg)
	print('------------------------------')


mensagem('     SISTEMA DE ALUNOS     ')
--------------------------------------------------------

def soma(a, b):
	s = a + b
	print(s)


# Main
soma(1, 4)  #5
soma(5, 5)  #10
soma(5, 10) #15
--------------------------------------------------------

def soma(a, b):
	print('--- A = {} e B = {} ---'.format(a, b))
	s = a + b
	print('{} + {} = {}'.format(a, b, s))
	print('')


# Main
soma(1, 4)  #5
soma(5, 5)  #10
soma(5, 10) #15
--------------------------------------------------------

