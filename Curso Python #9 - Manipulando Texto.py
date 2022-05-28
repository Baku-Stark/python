>>> Manipulando Texto

frase = 'Curso em Vídeo'

* Fatiamento
-- len(frase)
-- frase.count('example') >>> contar quantas letras tem.
-- frase.count('o', 0, 13) >>> contagem com FATIAMENTO
-- frase.find('deo') >>> encontrar a exata frase na posição da string
-- frase.find('ANDROID') >>> retorna com o valor '-1'
	-- frase.replace('Python', 'ANDROID') >>> Substituir frases
-- frase.upper() >>> deixar toda a string em maíusculo
-- frase.lower() >>> deixar toda a string em minúsculo
-- frase.capitalize() >>> transformar todos os caracteres em minúsculo, menos o primeiro caracter
-- frase.title() >>> analisar as palavras na string e transformar o primeiro caracter ápos o espaço
-- frase.strip() >>> remover os ESPAÇOS inúteis
	-- frase.rstrip() >>> remover os ESPAÇOS inúteis da DIREITA (RIGHT)
	-- frase.lstrip( >>> remover os ESPAÇOS inúteis da ESQUERDA (LEFT)
-- frase.split() >>> remove os ESPAÇOS e separa em uma lista
		-- '-'.join(frase) >>> junta toda a lista
-- 'Curso' in frase >>> Verificar certa frase (operador)
frase [9] --> Ler a letra usando o caracter;
frase [:5] --> Ler a string do caractere ZERO até o número selecionado (5);
frase [15:] --> Ler a string do caractere à partir do 15 (sem final);
frase [9::3] --> Ler a string até o final pulando duas casas;
frase [9:13] --> Ler uma cadeia fechada (não contando o último valor);
frase [9:21:2] --> Ler uma cadeia fechada (porém, pulando um caracter);
_______________________________________________________________________________________________________________________________________________________________

{-- TEST 09 --}

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'ZIKA LEK'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.lower().find('Curso'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print("""Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site cursoemvideo.com/apoie Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.""")
_______________________________________________________________________________________________________________________________________________________________

# Desafio 01
* Crie um programa que leia o nome completo de uma pessoa e mostre:
-- O nome com todos as letras maíusculas;
-- O nome com todas minúsculas;
-- Quantas letras ao todo (sem considerar espaços);
-- Quantas letras tem o primeiro nome.

nome = 'Wallace De Freitas Moura Dos Santos'
print(nome[0:8])
print(nome.lower())
print(nome.upper())
print(nome.count('Wallace'))

# Desafio 02
* Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados
EX: Digite um número: 1834 --->>> unidade: 4; dezena: 3; centea: 8; milhar: 1
import random 
num = random.randint(0, 9999)
print(num)

select = str(input('Número Gerado:'))
print('Unidade:{}'.format(select[3]))
print('Dezena:{}'.format(select[2]))
print('Centena:{}'.format(select[1]))
pritn('Milhar:{}'.format(select[0]))

# Desafio 03
* Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 
o nome "SANTO". 
city = str(input('Nome da Cidade/Bairro:')).strip().lower().capitalize()
print('Santo' in city[:5])

# Desafio 04
* Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" 
no nome.
nome = str(input('Nome Completo:')).strip().lower().capitalize()
print('Silva' in nome[:5])

# Desafio 05
* Faça um programa que leia uma frase pelo teclado e mostre:
-- Quantas vezes aparece a letra "A";
-- Em que posição ela aparece a primeira vez;
-- Em que posição ela aparece a última vez.
string = str(input('Digite algo:'))
print(string.count('A'))
print(string.find('A'))

# Desafio 06
* Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
EX: Wallace De Freitas Moura Dos Santos
primeiro = Wallace
último = Santos 

allname = str(input('Digite seu nome completo:')).split()

print('Primeiro Nome: {}'.format(allname[0]))
print('Último Nome: {}'.format(allname[len(allname) - 1])) 
