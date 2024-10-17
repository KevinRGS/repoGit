# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

ph = 0
ph = int (input ("Ingresa el valor de PH: "))
if ph > 7: 
    print ("Basic")
elif ph < 7:
    print ("Acidic")
else:
    print ("Neutral")