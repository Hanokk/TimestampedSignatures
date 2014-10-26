def SquareAndMultiply(base,exponent,number):
	y=1
	binary=bin(exponent)
	length=len(binary)
	for i in range((length-2)):
		if binary[(length-1)-i]=='1':
			y=(base*y)%number	
		base=(base*base)%number
	return y
