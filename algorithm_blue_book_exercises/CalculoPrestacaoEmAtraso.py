valor = int(input("Digite o valor da prestacao -> "))

taxa = int(input("Digite o valor da taxa -> "))

tempo = int(input("Digite o tempo de atraso -> "))

prestacao = valor + (valor + (taxa/100) * tempo)

print("Valor: ", prestacao)

