
L1 = [0, 1, 2, 3, 4]
L2 = [5, 6, 7, 8, 9]

print("Lista L1")
for x in L1:
    print(x)

print("Lista L2")
for x in L2:
    print(x)

print("Trocando os valores da lista...............")

for x in range(1, 5):
    print("L1 ->", L1[x])
    print("L2 ->", L2[x])
    #Captar os valores da lista
    a1 = L1[x]
    a2 = L2[x]

    L1.insert(a2, x)
    L2.insert(a1, x)

print("Fim do processo! Resultado da troca de valores")

print("Lista L1")
for x in L1:
    print(x)

print("Lista L2")
for x in L2:
    print(x)
