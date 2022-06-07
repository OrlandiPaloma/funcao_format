#funcao format.
nome = 'Paloma Daniela'
idade = 26
print( 'O nome do usuário é {} e ela tem {} anos'.format(nome, idade))
print()

#pode-se facilitar nomeando as posições dentro da função format e após chamando-as.

nome = 'Paloma Daniela'
idade = 26
print( 'O nome do usuário é {0} e ela tem {1} anos. Repetindo: o nome do usuario é {0} e ela tem {1} anos.'.format(nome, idade))
print()

#exemplo usando apenas a letra f:

print(f'O nome do usuário é {nome}. Essa variavel é do tipo 'f'{type(nome)}')
print('\n')

#teste TYPE:
print({type(nome)})
print({type(idade)})