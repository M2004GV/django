#a estrutura dicionario é um tipo de hashing
#onde eu acompanho o valor pelo identificador à esquerda
#um identificador só pode ser do tipo int, float, string
meu_dicionario = {'name': 'Paulo', 'idade': 20, 'filhos' : 1}

meu_dicionario['idade'] = 3
meu_dicionario['cidade'] = 'sao paulo'

print(meu_dicionario)

#alguns métodos dos dicionários

#retorna uma lista das chaves
meu_dicionario.keys()

#retorna uma lista dos valores
meu_dicionario.values()

#retorna uma lista dos itens(tuplas)
meu_dicionario.items()