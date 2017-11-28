def FindDivisors(numero):
	count = 1
	while count <= numero:
	  if numero % count == 0:
	    print (count)
	  count = count +1

print(FindDivisors(0))
print(FindDivisors(-1))
print(FindDivisors(7))
print(FindDivisors(15))
print(FindDivisors(70))
print(FindDivisors(250))


