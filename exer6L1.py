def triangulo(a, b, c):
  verifica = False
  if((b-c)*-1 < a and (b+c > a)):
    verifica= True
  else: verifica = False
  if((b-a)*-1 < c and (b+a > c)):
    verifica= True
  else: verifica = False  
  if((a-c)*-1 < b and (a+c > b)):    
    verifica= True
  else: verifica = False
  #ve tipo do triangulo
  if(verifica == True):
    if(a == b and b == c):
      return 'Equilátero'
    elif(a != b and a != c and c != b):
      return 'Escaleno'  
    else: return 'Isóceles'  



a = int(input())
b = int(input())
c = int(input())
print(triangulo(a, b, c))
