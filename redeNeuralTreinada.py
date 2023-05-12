import numpy

# [0.86, 0.62, 0.36, 0.56] =  0.6      chove
# [0.21, 0.05, 0.11, 0.28] =  0.1625   não
# [0.33, 0.97, 0.81, 0.77] =  0.72     chove
# [0.42, 0.69, 0.95, 0.50] =  0.64     chove
# [0.20, 0.04, 0.14, 0.22] =  0.15     não
# [0.76, 0.54, 0.91, 0.56] =  0.6925   chove
# [0.39, 0.17, 0.17, 0.32] =  0.2625   não
# [0.98, 0.80, 0.65, 0.70] =  0.7825   chove
# [0.22, 0.61, 0.76, 0.09] =  0.42     talvez
# [0.96, 0.53, 0.63, 0.71] =  0.7075   chove
# [0.25, 0.61, 0.80, 0.12] =  0.445     talvez
# [0.25, 0.61, 0.99, 0.12] =  0.4925    talvez
# [0.25, 0.61, 0.45, 0.12] =  0.3575    talvez
# [0.25, 0.61, 0.99, 0.12] =  0.4925    talvez
# [0.25, 0.34, 0.45, 0.12] =  0.29      não
# [0.29, 0.34, 0.45, 0.12] =  0.3       talvez
# [0.71, 0.64, 0.45, 0.56] =  0.59      talvez

# (0.86 + 0.62 + 0.36 + 0.56)/4 = 0.6      chove
# (0.21 + 0.05 + 0.11 + 0.28)/4 = 0.1625   não
# (0.33 + 0.97 + 0.81 + 0.77)/4 = 0.72     chove
# (0.42 + 0.69 + 0.95 + 0.50)/4 = 0.64     chove
# (0.20 + 0.04 + 0.14 + 0.22)/4 = 0.15     não
# (0.76 + 0.54 + 0.91 + 0.56)/4 = 0.6925   chove
# (0.39 + 0.17 + 0.17 + 0.32)/4 = 0.2625   não
# (0.98 + 0.80 + 0.65 + 0.70)/4 = 0.7825   chove
# (0.22 + 0.61 + 0.76 + 0.09)/4 = 0.42     talvez
# (0.96 + 0.53 + 0.63 + 0.71)/4 = 0.7075   chove
# (0.25 + 0.61 + 0.80 + 0.12)/4 = 0.445     talvez
# (0.25 + 0.61 + 0.99 + 0.12)/4 = 0.4925    talvez
# (0.25 + 0.61 + 0.45 + 0.12)/4 = 0.3575    talvez
# (0.25 + 0.61 + 0.99 + 0.12)/4 = 0.4925    talvez
# (0.25 + 0.34 + 0.45 + 0.12)/4 = 0.29      não
# (0.29 + 0.34 + 0.45 + 0.12)/4 = 0.3       talvez
# (0.71 + 0.64 + 0.45 + 0.56)/4 = 0.59      talvez


# 0.0 até 0.29 não chove
# 0.30 até 0.59 poucas chances
# 0.60 pra cima chove

# Probabilidade    Descrição
# 0%    Nenhuma chance de chuva
# ~10%    leve chance de chuvas isoladas
# ~20%    pequena chance de chover
# 30-50%    chance considerável de chuvas espalhadas
# 60-70%    chuvas espalhadas
# 80-100%    chuvoso (forte ou fraco)

saidas = numpy.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1])

entradas = numpy.array([
    [0.86, 0.62, 0.36, 0.56], 
    [0.21, 0.05, 0.11, 0.28], 
    [0.33, 0.97, 0.81, 0.77], 
    [0.42, 0.69, 0.95, 0.50], 
    [0.20, 0.04, 0.14, 0.22], 
    [0.76, 0.54, 0.91, 0.56], 
    [0.39, 0.17, 0.17, 0.32], 
    [0.98, 0.80, 0.65, 0.70], 
    [0.22, 0.61, 0.76, 0.09],
    [0.96, 0.53, 0.63, 0.71], 
    [0.25, 0.61, 0.80, 0.12], 
    [0.25, 0.61, 0.99, 0.12], 
    [0.25, 0.61, 0.45, 0.12], 
    [0.25, 0.61, 0.99, 0.12], 
    [0.25, 0.34, 0.45, 0.12], 
    [0.29, 0.34, 0.45, 0.12], 
    [0.71, 0.64, 0.45, 0.56], 
])

pesos = numpy.array([0.656, 0.932, 1.028, 0.45 ])
pesos1 = numpy.array([0.0, 0.0, 0.0, 0.0])
learning_rate = 0.1

def stepfunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepfunction(s)

# def treinar():
#     erroTotal = 1
#     while(erroTotal != 0):
#         erroTotal = 0
#         for i in range(len(saidas)):
#             saidaCalculada = calculaSaida(numpy.asarray(entradas[i]))
#             erro = abs(saidas[i] - saidaCalculada)
#             erroTotal += erro
#             for j in range(len(pesos)):
#                 pesos[j] = pesos[j] + (learning_rate * entradas[i][j] * erro)
#                 print('Peso atualizado: ', pesos)

#         print('Total de erros: ', erroTotal)

# treinar()

registro = numpy.array( [0.25, 0.34, 0.45, 0.12] )

if(calculaSaida(registro) == 0 ):
    print("Não chove, fica tranquilo")
elif(calculaSaida1() == 0):
    print("Pode chover um pouco")
else:
    print("Prepara o guarda-chuva, vai com toda certeza chover")