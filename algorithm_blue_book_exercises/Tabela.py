nome1 = "Ramon"
nome2 = "Dave"
nome3 = "Ramone"
nome4 = "Hayley"

print("Nome do aluno\t\tNota")
print("---------------------------------------------------------------")
print("%s:\t\t\t%f" % (nome1, 7.8))
print("%s:\t\t\t%f" % (nome2, 8.8))
print("%s:\t\t\t%f" % (nome3, 9.8))
print("%s:\t\t\t%f" % (nome4, 6.8))
print("---------------------------------------------------------------")

T = []

cont = True

while cont:
    nome = input("Digite o nome do aluno: ")
    nota = int(input("Digite o nome do aluno: "))

    A = []

    A.append(nome)
    A.append(nota)

    T.append(A)

    #Aluno.insert(nome);
    #Nota.insert(nota)

    for x in T:
        print("Nome do aluno\t\tNota")
        print("---------------------------------------------------------------")
        print("%s:\t\t\t%f" % (nome1, 7.8))
        print("%s:\t\t\t%f" % (nome2, 8.8))
        print("%s:\t\t\t%f" % (nome3, 9.8))
        print("%s:\t\t\t%f" % (nome4, 6.8))
        print("---------------------------------------------------------------")


