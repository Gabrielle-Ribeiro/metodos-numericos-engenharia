from math import e, cos


# Método da Bisseção
# Função utilizada
# Alterar a função para a função utilizada no problema

def f(x):
  return e ** (-x**2) - cos(x)

# Dados iniciais
# Alterar dados iniciais para os dados utilizados no problema

# Intervalo inicial [a, b]
a = 1
b = 2

# Precisão
precisao = 0.001

# Nº máximo iterações
k_maximo = 50

#------------------------------------------------------------------

def bissecao(a, b, precisao, k_maximo):
    k = 1 # Nº Iteração
  
    while(k <= k_maximo):
        x = (a + b) / 2
    
        print(f'X{k} = {x}')
        print(f'f(x) = f({x}) = {f(x)}')
        print(f'f(a) = f({a}) = {f(a)}')
        print(f'f(b) = f({b}) = {f(b)}')
        print('\n')

        # Critério de parada
        if b - a < precisao:
            return x

        if (f(a)*f(x)) > 0:
            a = x
        else:
            b = x

        k += 1

    return x

print(bissecao(a, b, precisao, k_maximo))