
# Matriz é uma representação de dados, geralmente numéricos, divididos por linhas e colunas. Uma matriz é
# representada da forma Amxn. Assim, temos a matriz A, que possui m linhas e n colunas. A matriz M3x2,
# por exemplo, possui três linhas e duas colunas. A matriz contém termos representados por aij, em que i é
# a linha que o termo ocupa e j é a coluna que o termo ocupa.
#
# Existem casos especiais de matriz, como a matriz linha, a matriz coluna, a matriz quadrada, a matriz
# oposta e a matriz identidade. Podemos realizar operações importantes com as matrizes, como adição, subtração
# e multiplicação. Na informática, matrizes são essenciais para o desenvolvimento da programação. A matriz
# é utilizada para facilitar o trabalho com dados numéricos, separando determinadas informações de tabelas
# por linhas e colunas.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

boletim = []
# range(start, stop, step)
for x in range(1, 3):
	for y in range(0, 3):
		matriz[x][y] = int(input(f'Digite a nota {y} do aluno {x}: '))

for x in range(0, 3):
	for y in range(0, 3):
		print(f'[{matriz[x][y]:^5}]', end='')
	print()
print("-------------------------------------")
