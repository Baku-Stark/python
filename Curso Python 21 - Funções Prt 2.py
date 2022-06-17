Aula 21 – Funções (Parte 2)

'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre 
Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos 
opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''

--->>> Interactive Help
--- help()
print("string exemplo (input, print, etc".__doc__)

###

#Fazendo Docstring
def function(i, f, p):
	"""
	-> Faz uma contagem e mostra na tela.
	:param i: Início da contagem
	:param f: Fim da contagem
	:param p: Passo da contagem
	:return: Sem retorno
	Função criada por Wallace de Freitas
	"""
	c = i
	while c <= f:
		print('{}'.format(c)),
		c += p
	print('Fim!')

function(2, 10, 2)
help(function)

--->>> Parâmetros opcionais

def somar(a=0, b=0, c=0):
	"""
	-> Faz a soma dos números e mostra na tela.
	:param a: 1° Valor
	:param b: 2° Valor
	:param c: 3° Valor
	:return: Sem retorno
	Função criada por Wallace de Freitas
	"""
	s = a + b + c
	print('A soma vale {}'.format(s))

somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)

--->>> Escopo de Variáveis

def teste():
	x = 8
	print('Na função teste, n vale {}.'.format(n))
	print('Na função teste, x vale {}.'.format(x))


# -----
n = 2
teste()
print('No programa principal, n vale {}.'.format(n))


def teste(b):
	global a
	a = 8
	b += 4
	c = 2
	print('[A] dentro vale {}.'.format(a))
	print('[B]dentro vale {}.'.format(b))
	print('[C]dentro vale {}.'.format(c))


# ---
a = 5
teste(a)
print('[A] fora vale {}.'.format(a))


--->>> Retornando Valores
def somar(a=0, b=0, c=0):
	s = a + b + c
	return s


# ===
resp1 = somar(3, 2, 5)
resp2 = somar(2, 2)
resp3 = somar(6)
print('Todas as somas foram: {} {} e {}'.format(resp1, resp2, resp3))
--------------------------------------------------------

def fatorial(num=1):
	f = 1
	for c in xrange(num, 0, -1):
		f *= c
	return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print('Os resultados são {} {} e {}'.format(f1, f2, f3))

###

def par(n=0):
	if n % 2 n == 0:
		return True
	else:
		return False

num = int(input('Digite um número: '))
if par(num):
	print('É par!')
else:
	print('É impar!')
