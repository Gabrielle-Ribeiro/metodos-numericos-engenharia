# Modificar

x = [0]
y = [2]

h = 0.2

a = 0
b = 1

# Modificar

def f(x, y):
    return x - y + 2

#-------------------------------------------------

m = int((b - a)/h)

for i in range(m+1):
    x_anterior = x[i]
    y_anterior = y[i]

    k1 = f(x_anterior, y_anterior)
    k2 = f(x_anterior + h, y_anterior + h * k1)

    new_x = x_anterior + h
    new_y = y_anterior + (h/2) * (k1 + k2)

    x.append(new_x)
    y.append(new_y)

for i in range(m+1):
    print(f"x{i} = {x[i]}")
    print(f"y{i} = {y[i]}\n")