from math import log
# Método do Ponto Fixo

# Função utilizada
# Alterar a função para a função utilizada no problema

def f(x):
  return x * log(x, 10) - 1

# Função de iteração
# Alterar a função para a função utilizada no problema

def f_iteracao(x):
  return 1 / log(x, 10)

# Dados iniciais
# Alterar dados iniciais para os dados utilizados no problema

# X inicial deve pertencer ao intervalo [a, b]
x_inicial = 2.5

# Precisão (Se o problema não der precisao2: precisao2 = precisao1)
precisao1 = 0.01
precisao2 = 0.01

# Nº máximo iterações
k_maximo = 50

#-----------------------------------------------------------------

def ponto_fixo(precisao1, precisao2, k_maximo, x_inicial):
    x0 = x_inicial
    
    #if abs(f(x0)) < precisao1:
        #return x0
    
    k = 1
    while(k <= k_maximo):
        x1 = f_iteracao(x0)

        print(f'X{k} = {x1}')
        print(f'f_iteracao({x0}) = {f_iteracao(x0)}')
        print(f'f({x1}) = {f(x1)}')
        print('\n')

        if abs(f(x1)) < precisao1:
            return x1

        #if abs(x1 - x0) < precisao2:
            #return x1

        x0 = x1
        k += 1

    return x0

print(ponto_fixo(precisao1, precisao2, k_maximo, x_inicial))