import millerrabin
def Prime(Number):
	prime=Number-1
	while True:
		if Number%(prime)==0:
			check=millerrabin.MillerRabin(prime)
			if check:
				break
			else:
				prime=prime-1
		else:
		    prime=prime-1
	return prime
		
    
