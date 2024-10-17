credits = int (input ("ingresa tus creditos: "))
height = float (input ("ingresa tu altura: "))

if credits >= 10 and height >= 1.50:
    print ("Enjoy the ride")
elif credits >= 10 and height < 1.50:
    print ("You are not tall enough to ride")
elif credits < 10 and height >= 1.50:
    print ("You don't have enough credits")
else: 
    print ("You don't meet requirements")