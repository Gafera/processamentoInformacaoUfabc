def anoBissexto(a):
  if(int(a) % 4 == 0 or int(a) % 400 == 0):
    return 'Verdadeiro'
  elif(int(a) % 100 != 0):
    return 'Falso'




a = input()
print(anoBissexto(a))
