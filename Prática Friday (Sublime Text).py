from time import sleep
res = 3
while res >= 3:
	print('''Ol�, senhor Stark!
	O que o senhor deseja?''')
	print('''
		[ 1 ] verificar

		[ 2 ] pular etapa
		''')
	res = int(input('Deseja verificar o sistema da >Mark Deos Prime<? \nr: '))
	print('')
	print('-=-' *5)
	print('')
	if res == 1:
		print('Acessando banco de dados....')
		print('90%...')
		sleep(1)
		print('92%...')
		sleep(1)
		print('99%...')
		sleep(1.5)
		print('100%...')
		print('''Acesso Liberado!
		Bem-Vindo, senhor Stark''')
		print('Iniciando Sistema...')
		print('Armas --------------------- OK!')
		print('Nanoteclogia do n�cleo ---- OK!')
		print('Monitor e Comunica��o ----- OK!')
		print('-=-' *5)
		break
	elif res == 2:
		print('>>> Pulando etapa de verifica��o')
		break
		print('-=-' *5)
	else:
		print('>>> Resposta Errada... Fa�a novamente!')
	print('')
	print('-=-' *5)
print('')
print('> Verifica��o Finalizada!!! <')