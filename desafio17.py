from math import pow
b = float(input('digite o co '))
c = float(input('digite o ca '))
bc = pow(b, 2) + pow(c, 2)
a = pow(bc, 1/2)
print('O cateto adjacente é {}'.format(c)) 
print('O cateto oposto é {}'.format(b))
print('e a hipotenusa é {:.2f}'.format(a))
