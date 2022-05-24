Aula 19 – Dicionários

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome']) -- Pedro
print(dados['idade']) -- 25

> Adicionar elemento:
dados['sexo'] = 'M'

> Eliminar elemento:
del dados['idade']

EXEMPLO:
filme = {'título':'Star Wars',
		'ano':1977,
		'diretor': 'George Lucas'
		}
print(filme.values())
-- todos os primeiros valores = 'Star Wars', 1977, 'George Lucas'

print(filme.keys())
-- todas as chaves do elemento = 'título', 'ano', 'diretor'

print(filme.items())
-- pegar todos os métodos no laço (values e keys)
for k, v in filme.items():
	print('O {} é {}'.format(k, v))