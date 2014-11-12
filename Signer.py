import sys
import PrimeDivisor
import random
import FastExponentiation
import hashlib
import time
import timeit
from time import gmtime, strftime

__g__=2
__prime__=10007
__ys__=0
__yn__=0

def Hash(string):
	hash1=hashlib.sha1()
	hash1.update(string)
	sha_hex=hash1.hexdigest()
	output=int(sha_hex,16)
	return output

def Signature(Message):
	global __g__,__ys__,__prime__
	q=PrimeDivisor.Prime(__prime__-1)
	k1=random.randint(1,q)
	xs=random.randint(0,q-1)
	__ys__=FastExponentiation.SquareAndMultiply(__g__,xs,__prime__)
	start_time = time.clock()
	print start_time
	r1=FastExponentiation.SquareAndMultiply(__g__,k1,__prime__)
	e1=Hash(Message+str(r1))
	s1=(e1*xs+k1)%q
	print len(str(e1))
	#WithoutTimestamp(s1,e1,Message);
	elapsed=time.clock()-start_time
	TSS(q,s1,r1,e1,Message)


def TSS(q,s1,r1,e1,Message):
	global __g__, __yn__,__prime__
	xn=random.randint(0,q-1)
	__yn__=FastExponentiation.SquareAndMultiply(__g__,xn,__prime__)
	t=strftime("%Y-%m-%d %H:%M:%S", gmtime())
	k2=random.randint(1,q)
	r2=FastExponentiation.SquareAndMultiply(__g__,k2,__prime__)
	e2=Hash(t+str(e1)+str(r2))
	s=(k2-e2*(e1*xn+s1))%q
	print s,t,e2,r2
	WithTimestamp(t,s,r1,e2,Message)
	
def WithoutTimestamp(s1,e1,Message):
    global __g__,__yn__,__ys__,__prime__
    q=FastExponentiation.SquareAndMultiply(__ys__,e1,__prime__)
    r1=FastExponentiation.SquareAndMultiply(__g__,s1,__prime__)*pow(q,__prime__-2,__prime__)
    r11=FastExponentiation.SquareAndMultiply(r1,1,__prime__)
    print r11
    output=Hash(Message+str(r11))
    print output

def WithTimestamp(t,s,r1,e2,Message):
    global __g__,__prime__,__ys__,__yn__
    e1=Hash(Message+str(r1))
    temp=e1*e2
    temp1=FastExponentiation.SquareAndMultiply(__ys__*__yn__,temp,__prime__)
    temp2=FastExponentiation.SquareAndMultiply(r1,e2,__prime__)
    out=(FastExponentiation.SquareAndMultiply(__g__,s,__prime__)*temp1*temp2)%__prime__
    final=Hash(t+str(e1)+str(out))
    print final

Signature('hanok galaba')	