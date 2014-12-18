def ExtendedEuclidean(b,n):
	r1=n
	r2=b
	t1=0
	t2=1
	while r2>0:
		q=r1/r2
		r=r1-(q*r2)
		r1=r2
		r2=r

		t=t1-(q*t2)
		t1=t2
		t2=t

	if r1==1:
		return t1%n