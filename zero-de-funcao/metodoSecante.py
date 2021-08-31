# Método da Secante

# Função utilizada
# Alterar a função para a função utilizada no problema

def f(x):
  return x**3 - 9*x + 3

# Dados iniciais
# Alterar dados iniciais para os dados utilizados no problema

# X inicial pode ser qualquer ponto da reta
x0 = 0
x1 = 1

# Precisão (Quando não tiver precisão2: precisão2 = precisão1 )
precisao1 = 0.0005
precisao2 = 0.0005

# Nº máximo iterações
k_maximo = 50

def metodo_secante(x0, x1, precisao1, precisao2, k_maximo):
    if abs(f(x0)) < precisao1:
        return x0

    if abs(f(x1)) < precisao1: 
        return x1

    #if abs(x1 - x0) < precisao2:
        #return x1

    k = 1

    while(k <= k_maximo):
        x = (x0*f(x1) - x1*f(x0)) / (f(x1) - f(x0))

        print(f'Iteracao: {k}')
        print(f'X{k} = {x}')
        print(f'f({x}) = {f(x)}')
        print('\n')

        # Critério de parada
        if abs(f(x)) < precisao1:
            return x
            
        #if abs(x - x1) < precisao2:
            #return x

        x0 = x1
        x1 = x

        k += 1

    return x

print(metodo_secante(x0, x1, precisao1, precisao2, k_maximo))