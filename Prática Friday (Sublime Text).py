from time import sleep
res = 3
while res >= 3:
	print('''Olá, senhor Stark!
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
		print('Nanoteclogia do núcleo ---- OK!')
		print('Monitor e Comunicação ----- OK!')
		print('-=-' *5)
		break
	elif res == 2:
		print('>>> Pulando etapa de verificação')
		break
		print('-=-' *5)
	else:
		print('>>> Resposta Errada... Faça novamente!')
	print('')
	print('-=-' *5)
print('')
print('> Verificação Finalizada!!! <')