dn=int(input('enter any decimal number:'))
resulting=[]
while dn>0:
	resulting.append(dn%2)
	dn=dn//2
resulting.reverse()
for dn in  resulting:
	print(dn,end="")
	