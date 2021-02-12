from math import sin, cos, tan
a = int(input('Digite um ângulo '))
s = sin(a)
c = cos(a)
t = tan(a)
print('O ângulo é {}'.format(a))
print('O seu senon é {:.3f},'.format(s))
print('seu cosseno é {:.3f},'.format(c))
print('e sua tangente é {:.3f}'.format(t))
