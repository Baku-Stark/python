>>> Curso Python #11 - Cores no Terminal

ANSI - escape sequence

\033[0;33;44m
STYLE			TEXT			       FUNDO
0 Nenhum		30				40			Branco
1 Negrito		31				41			Vermelho
4 Sublinhado		32				42			Verde
7 Inverter		33				43			Amarelo
			34				44			Azul
			35				45			Roxo
			36				46			Ciano
			37 				47			Cinza

Exemplo prático
print('\033[1;36;47mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[36m{}\033[m e \033[34m{}\033[m!!!'.format(a, b))

print('Olá, \033[1;36mWallace\033[m! Bem-Vindo ao \033[33mPython\033[m!')

nome = 'Wallace'
print('olá, {}{}{}. Muito prazer em conhcer você!'.format('\033[4;36m', nome, '\033[m'))

nome = 'Wallace'
cores = dict(limpa='\033[m', azul='\033[34m', amarelo='\033[33m', pretobranco='\033[7;30m')
print('olá, {}{}{}. Muito prazer em conhocer você!'.format(cores['azul'], nome, cores['limpa']))
___________________________________
nome = 'Wallace'
cores = dict(limpa='\033[m',
             azul='\033[34m',
             amarelo='\033[33m',
             pretobranco='\033[7;30m')
print('olá, {}{}{}. Muito prazer em conhocer você!'.format(cores['pretobranco'], nome, cores['limpa']))
