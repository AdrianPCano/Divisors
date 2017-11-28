numero = int(input("Dime un numero:"))
count = 1

while count <= numero:
  if numero % count == 0:
    print (count)
  count = count +1