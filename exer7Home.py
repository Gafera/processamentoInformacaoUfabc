def segundo_maior(lista, n):
  lista.sort()
  return lista[n-2]
  
n = int(input())
lista = []
for i in range(0, n):
    k = int(input())
    lista.append(k)
print(segundo_maior(lista, n))
