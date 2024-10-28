p = int(input("Digite um Número Inteiro "))
sequencia = []
valor = False

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        return sequencia.append(0)
    elif n == 1:
        return sequencia.extend([0,1])
    else:
        sequencia.append(0)
        while b <= n:
            sequencia.append(b)
            b = b + a
            a = b - a
        if b > n:
            return sequencia

fibonacci(p)
for i in range(0,len(sequencia)):
    if sequencia[i] == p:
        valor = True
        break
if valor == True:
    print("O número {} pertence a sequência de Fibonacci".format(p))
else:
    print("O número {} não pertence a sequência de Fibonacci".format(p))














