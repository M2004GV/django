#é permitido tanto aspas simples como duplas
minha_string = 'Mateus'

print(minha_string)

#pra ver quantos caracters tem uma string
print(len(minha_string))

minha_string1 = 'Fernando'

minha_string2 = minha_string1 + ' '+ minha_string
print(minha_string2)

#selecao em range
#a esquerda do ':' diz onde inicia(inclui) e 
#a direita do ':' diz (exclui)
print(minha_string[1:])

# indexação com '::' pulo de intervalos
print(minha_string[::2])

print("hello world".split("w"))

#funcao para contar determinado caracter
num = minha_string.count('a')
print(num)

#funcao para encontrar um substring numa string
print(minha_string.find('teus'))

#caixa alta 
#.upper()
#caixa baixa 
#.lower()

#primeira maiúscula
#.capitalize() ou .title() para mais de uma palavra

#remover os espaços em branco
#.strip() .rstrip() .lstrip()