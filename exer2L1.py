global verifica
def verificacao(a, m, d):
  
  if(a >= 1):
    print('Verificando...')
    verifica = True
  if(m >= 1 and m <= 12 and verifica == True):
    print('Verificando...')
  else:
     verifica = False
  if(d >= 1 and d <= 31 and verifica == True):
    print('Verificando...')
  else:
    verifica = False
  #----------------formula---------------
  #a0=a−(14−m)//12
  aInicial = a-(14-m)//12
  x = aInicial + aInicial//4 - aInicial//100 + aInicial//400
  mesInicial = m + 12 * ((14-m)//12)-2
  dInicial = (d+x+(31*mesInicial)//12)%7
 
  if(dInicial == 0 ):
    return 'Domingo'
  elif(dInicial == 1 ):
    return 'Segunda'
  elif(dInicial == 2 ):
    return 'Terça'
  elif(dInicial == 3 ):
    return 'Quarta'
  elif(dInicial == 4 ):
    return 'Quinta'
  elif(dInicial == 5 ):
    return 'Sexta'
  elif(dInicial == 6 ):
    return 'Sábado'
aInicial = 0
x = 0
mesInicial = 0
dInicial = 0
a = int(input('Ano: '))
m = int(input('Mês: '))
d = int(input('Dia do mês: '))
print(verificacao(a, m, d))
