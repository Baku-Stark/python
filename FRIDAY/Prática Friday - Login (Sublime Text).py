#Login da armadura MD. Prime
print('-=' *30)
username = ''
senhapass = ''
user = input('>> Username: ')
if user == '---':
	#print('usuário confirmado!')
	username = True
else:
	print('\033[1;31mUsuário não encontrado\033.')
senha = input('>> Senha: ')
if senha == '---':
	#print('senha confirmada!')
	senhapass = True
else:
	print('\033[1;31mSenha incorreta.')
print('')
if username == True and senhapass == True:
	print('--- LOGIN REALIZADO COM SUCESSO! BEM-VINDO {}! ---'.format(user))
else:
	print('--- VERIFIQUE SEU NOME DE USUÁRIO E/OU SENHA. ---')
print('-=' *30)
print('')
