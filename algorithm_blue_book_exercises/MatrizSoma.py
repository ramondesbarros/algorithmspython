m1 = [[0,0,0],[0,0,0],[0,0,0]]
m2 = [[0,0,0],[0,0,0],[0,0,0]]
ms = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(0, 3):
	for y in range(0, 3):
		m1[x][y] = int(input(f'Digite um valor para m1: [{x}, {y}]: '))

for x in range(0, 3):
	for y in range(0, 3):
		m2[x][y] = int(input(f'Digite um valor para m2: [{x}, {y}]: '))

for x in range(0, 3):
	for y in range(0, 3):
		ms[x][y] = m1[x][y] + m2[x][y]

for x in range(0, 3):
	for y in range(0, 3):
		#rint(f'[{matriz[x][y]:^5}]', end='')
		print(f'{ms[x][y]} ', end='')
	print()