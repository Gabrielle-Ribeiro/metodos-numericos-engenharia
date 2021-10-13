from math import log

a = 1
b = 2
precisao = 0.001

k = (log(b-a, 10) - log(precisao, 10)) / log(2,10)
print(k)