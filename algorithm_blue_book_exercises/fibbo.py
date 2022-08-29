# n = 0
# s = 1
# l = 1000
# while (l > 0):
#     n = n + s
#     print("--> ", n)
#     s = n
#
#     l = l-1

print (" Trabalho de Fibonacci ")

n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print("{}.".format(t3), end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print( " Fim ")