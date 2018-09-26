import os
#x=detx/detcoeff
#y=dety/detcoeff

neq=input("Matrice quadrata(2x2) o Rettangolare(3x3)? (inserisci solo quadrata o rettangolare) ")
neq=neq.lower()


coeff=[]
ris=[]

if neq=="quadrata":
	for i in range(4):
		c1=int(input("Inserisci coeff uno alla volta (per righe) "))
		coeff.append(c1)

	domanda1=input("Sono giusti (si o no)?  ")
	domanda1=domanda1.lower()
	if domanda1=="si":
		print("Procediamo")
	elif domanda1=="no":
		print("Ricomincia")
		exit()


	print(coeff)
	for a in range(2):
		r1=int(input("Inserisci i  risultati uno alla volta  "))
		ris.append(r1)

	print(ris)



	
	domanda=input("Sono giusti (si o no)?  ")
	domanda=domanda.lower()
	
	if domanda=="si":
		print("Procediamo")
	elif domanda=="no":
		print("Ricomincia")
		exit()

	vuot=input("Premi invio per continuare")
	os.system("cls")

	diagMc= coeff[0]*coeff[3]
	diagmc= coeff[1]*coeff[2]

	detcoeff= diagMc-diagmc


	print("Questi sono, in ordine, il determinante mat. coefficiente, il determinante mat. x e il determinante mat. y")
	#print(diagmc)
	#print(diagMc)
	print(detcoeff)

	diagMx=ris[0]*coeff[3]
	diagmx=ris[1]*coeff[1]
	detx=diagMx-diagmx


	#print(diagMx)
	#print(diagmx)
	print(detx)

	diagMy=coeff[0]*ris[1]
	diagmy=coeff[2]*ris[0]
	dety=diagMy-diagmy

	#print(diagMy)
	#print(diagmy)
	print(dety)


	x=detx/detcoeff
	y=dety/detcoeff

	print("QUESTE CHE SEGUONO SONO LE SOLUZIONI, SEI PRONTO?")
	wkcn=input("Premi invio per continuare")
	print("...")
	print("...")
	wkcl=input("Premi invio per continuare")
	os.system("cls")

	x=int(x)
	y=int(y)

	print("x è:")
	print()
	print(x)

	print()
	print()

	print("y è : ")
	print()
	print(y)




elif neq=="rettangolare":
	for i in range(9):
		c1=int(input("Inserisci coeff uno alla volta (per righe) "))
		coeff.append(c1)

	domanda1=input("Sono giusti (si o no)?  ")
	domanda1=domanda1.lower()
	if domanda1=="si":
		print("Procediamo")
	elif domanda1=="no":
		print("Ricomincia")
		exit()


	print(coeff)
	for a in range(3):
		r1=int(input("Inserisci i  risultati uno alla volta  "))
		ris.append(r1)

	print(ris)



	
	domanda=input("Sono giusti (si o no)?  ")
	domanda=domanda.lower()
	
	if domanda=="si":
		print("Procediamo")
	elif domanda=="no":
		print("Ricomincia")
		exit()



	f=coeff[0]*coeff[4]*coeff[8]
	v=coeff[1]*coeff[5]*coeff[6]
	l=coeff[2]*coeff[3]*coeff[7]

	diagMc= f+v+l


	n=coeff[2]*coeff[4]*coeff[6]
	m=coeff[0]*coeff[5]*coeff[7]
	o=coeff[1]*coeff[3]*coeff[8]

	diagmc= m+n+o

	print("In ordine stampo determinante matr .coeff, determinante matr .x, determinante matr. y, determinante matr. z")
	detcoeff= diagMc-diagmc
	
	print(detcoeff)





	q=ris[0]*coeff[4]*coeff[8]
	p=coeff[1]*coeff[5]*ris[2]
	r=coeff[2]*ris[1]*coeff[7]

	#print(q)
	#print(p)
	#print(r)

	diagMx= q+p+r


	s=coeff[2]*coeff[4]*ris[2]
	t=ris[0]*coeff[5]*coeff[7]
	u=coeff[1]*ris[1]*coeff[8]

	diagmx= s+t+u
	

	detx= diagMx-diagmx
	
	print(detx)


	ck=coeff[0]*ris[1]*coeff[8]
	j=ris[0]*coeff[5]*coeff[6]
	k=coeff[2]*ris[2]*coeff[3]

	

	diagMy= ck+j+k


	ra=coeff[2]*coeff[6]*ris[1]
	lu=ris[2]*coeff[0]*coeff[5]
	xc=coeff[3]*ris[0]*coeff[8]

	diagmy= ra+lu+xc
	

	dety=diagMy-diagmy
	
	print(dety)



	re=coeff[0]*coeff[4]*ris[2]
	loo=coeff[1]*ris[1]*coeff[6]
	rid=ris[0]*coeff[3]*coeff[7]

	diagMz= re+loo+rid


	sa=ris[0]*coeff[4]*coeff[6]
	sw=coeff[0]*ris[1]*coeff[7]
	lw=coeff[1]*coeff[3]*ris[2]

	diagmz= sa+sw+lw

	detz=diagMz-diagmz


	print(detz)


	x=detx/detcoeff
	y=dety/detcoeff
	z=detz/detcoeff

	print("QUESTE CHE SEGUONO SONO LE SOLUZIONI, SEI PRONTO?")
	wkcn=input("Premi invio per continuare")
	print("...")
	print("...")
	wkcl=input("Premi invio per continuare")
	os.system("cls")

	x=int(x)
	y=int(y)
	z=int(z)

	print("x è:")
	print()
	print(x)

	print()
	print()

	print("y è : ")
	print()
	print(y)

	print()
	print()

	print("z è : ")
	print()
	print(z)




















