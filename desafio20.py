import random
a1 = str(input('Primeiro nome '))
a2 = str(input('Segundo nome '))
a3 = str(input('Terceiro nome '))
a4 = str(input('Quarto nome '))
classe1 = (a1, a2)
classe2 = (a3, a4)
l1 = random.choices(classe1, cum_weights=None, k=2)
l2 = random.choices(classe2, cum_weights=None, k=3)
print('Os alunos são \n{}, \n{}, \n{}, \n{}.'.format(a1, a2, a3, a4))
print('A sequencia de apresentação do trabalho será \n{}, \n{}.'.format(l1, l2))
