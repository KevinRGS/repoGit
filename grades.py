#en el caso de condicionales, sebe estar identada la accion a realiar y siempre van : al final de la condicion
import random
grade = random.randint (1,100) #el modulo random genera un numero en este caso entre 1 y 100
print (grade)
if grade > 60:
  print("You passed.")
else:
  print("You failed.")