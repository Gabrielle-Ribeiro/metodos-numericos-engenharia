# Método de Newton-Raphson

# Função utilizada
# Alterar a função para a função utilizada no problema

def f(x):
  return x**3 - 9*x + 3

# Derivada da função
# Alterar a função para a função utilizada no problema

def f_derivada(x):
  return 3 * x**2 - 9

# Dados iniciais
# Alterar dados iniciais para os dados utilizados no problema

# X inicial pode ser qualquer ponto da reta, porém se estiver fora do intervalo
# a convergência demora mais
x_inicial = 1.5

# Precisão
precisao1 = 0.0005
precisao2 = 0.0005

# Nº máximo iterações
k_maximo = 50

#----------------------------------------------------------

def newton_raphson(precisao1, precisao2, x_inicial, k_maximo):
    k = 1
    x0 = x_inicial

    # Critério de parada
    if abs(f(x0)) < precisao1:
        return x0

    while(k <= k_maximo):
        x1 = x0 - (f(x0) / f_derivada(x0))

        print(f'X{k} = {x1}')
        print(f'f({x1}) = {f(x1)}')
        print('\n')

        # Critério de parada
        if abs(f(x1)) < precisao1:
            return x1

        #if abs(x1 - x0) < precisao2:
            #return x1

        x0 = x1
        k += 1

    return x0

print(newton_raphson(precisao1, precisao2, x_inicial, k_maximo))