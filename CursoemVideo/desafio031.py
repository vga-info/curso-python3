# DESAFIO 031
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS.

# Solicita ao usuário a distância da viagem em quilômetros
km = float(input('Digite quantos KMs tem a viagem: '))

# Verifica se a viagem é de até 200 KM
if km <= 200:
    # Calcula o preço da passagem para viagens de até 200 KM
    passagem = km * 0.50
else:
    # Calcula o preço da passagem para viagens acima de 200 KM
    passagem = km * 0.45

# Exibe o valor da passagem formatado com duas casas decimais
print(f'Valor da passagem: R${passagem:.2f}')
