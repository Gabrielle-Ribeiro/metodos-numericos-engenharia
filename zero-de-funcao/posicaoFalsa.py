from math import log

# Método da Posição Falsa

# Função utilizada
# Alterar a função para a função utilizada no problema
def f(x):
  return x * log(x, 10) - 1

# Dados iniciais
# Alterar dados iniciais para os dados utilizados no problema

# Intervalo inicial [a, b]
a = 2
b = 3

# Precisão (Se o problema não der precisao2: precisao2 = precisao1)
precisao1 = 0.01
precisao2 = 0.01

# Nº máximo iterações
k_maximo = 50

#------------------------------------------------------------------

def posicao_falsa(a, b, precisao1, precisao2, k_maximo):

    #if abs(f(a)) < precisao2:
        #return a
    
    #if abs(f(b)) < precisao2:
        #return b

    k = 1

    while(k <= k_maximo):
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))

        print(f'X{k} = {x}')
        print(f'f(x) = f({x}) = {f(x)}')
        print(f'f(a) = f({a}) = {f(a)}')
        print(f'f(b) = f({b}) = {f(b)}')
        print('\n')

        # Critério de parada
        #if abs(f(x)) < precisao2:
            #return x

        if (b - a) < precisao1:
            return x
    
        if f(a) * f(b) > 0:
            a = x
        else:
            b = x

        k += 1

    return x

print(posicao_falsa(a, b, precisao1, precisao2, k_maximo))