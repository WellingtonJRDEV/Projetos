import random
a1 = str(input('digite o nome do aluno 1 '))
a2 = str(input('digite o nome do aluno 2 '))
a3 = str(input('digite o nome do aluno 3 '))
a4 = str(input('digite o nome do aluno 4 '))
sorteio = random.choice ([a1, a2, a3, a4])
print('Haverá um sorteio para determinar quem vai apagar o quadro')
print('Os concorrentes são \n{}, \n{}, \n{} \ne {}'.format(a1, a2, a3, a4))
print('O sorteado foi """""" {} """""" '.format(sorteio))
