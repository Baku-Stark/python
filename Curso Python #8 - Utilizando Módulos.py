>>> Utilizando Módulos

Bebida Comida Doce

--> import + bebida 	comando Generalizado
--> from + doce + import = pudim	comando Específico
--------------------------------------------------------
import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz quadrada é: {}'.format(raiz))

import random 
num = random.randint(1, 10)
print(num)

* Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porçã inteira.
Ex: Digite um número: 6.127
O número de {6.127} tem a parte inteira {6}

import math
num = float(input('Digite um número:'))
rs = math.floor(num)
print('O valor inteiro é {}'.format(rs))

{----- DESAFIOS -----}

* Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo, calcule e mostre o comprimento da
hipotenusa.
(fórmula = a**2 = b**2 + c**2)
catop = int(input('Digite o Cateto Oposto:'))
catadj = int(input('Digite o Cateto Adjacente:'))
hipo = catop**2 + catadj**2
hipored = hipo **(1/2)
print('A hipotenusa é: {}'.format(hipored))

* Faça um programa que leia um ângulo  qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.
import math
a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))

* Um professor quer sortear um dos seus quatro alunos para apagar  quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do 
escolhido.
1 = Tony Stark
2 = Thor
3 = Bruce Banner
4 = Steve Rogers
import random
aluno = random.randint(1, 4)
print(aluno)

* O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
shuffle(lista)
print("A ordem de apresentação será")
print(lista)

* Faça um programa em Pythom que abra e reproduza o áudio de um arquivo MP3.
import pygame
import os
pygame.init()
if os.path.exists('musica.mp3'):
  pygame.mixer.music.load('musica.mp3')
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(1)

  clock = pygame.time.Clock()
  clock.tick(10)

  while pygame.mixer.music.get_busy():
     pygame.event.poll()
     clock.tick(10)
else:
  print('O arquivo musica.mp3 não está no diretório do script Python')