n = int(input('Digite um número inteiro '))
ta = (n + 0, n + 1, n + 2, n + 3, n + 4, n + 5, n + 6, n + 7, n + 8, n + 9)
tm = (n * 0, n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9)
td = (n / 1, n / 2, n / 3, n / 4, n / 5, n / 6, n / 7, n / 8, n / 9, n / 10)
ts = (n - 0, n - 1, n - 2, n - 3, n - 4, n - 5, n - 6, n - 7, n - 8, n - 9)
print('tabuada do número {}.'.format(n))
print(td, tm, ta)
