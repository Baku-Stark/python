Aula 23 - Tratamento de Erros e Exceções

print(x)
O termo 'x' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a grafia do nome 
ou, se um caminho tiver sido incluído, veja se o caminho está correto e tente novamente.
No linha:1 caractere:119
+ ... 310/python.exe c:/Users/-----/Desktop/Script/__pycache__/print(x).py
+                                                                     ~
    + CategoryInfo          : ObjectNotFound: (x:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

n = int(input('Digite um número: '))
n = int(input('Digite um número: '))
ValueError: invalid literal for int() with base 10: 'oito'

try:
	operação
except TypeError:
	falhou
else:
	deu certo
finally:
	certo/falha
--------------------------
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Infelizmente o cálculo falhou! :(')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dedos!')
except Exception as erro:
	print('O erro encontrado foi {}.'.format(erro.__cause__))
else: 
    print('O resultado é: {}'.format(r))
finally:
    print('VOLTE SEMPRE!')
