def mcd(a, b):
    resto = 0
    while(b > 0):
        d = b
        b = a % b
        a = d
    return a

m = int(input("Primeiro número: "))
n = int(input("Segundo número:"))

 

print("O máximo divisor comum de ", m," e ", n," é ", mcd(m, n))
