import PrimeDivisor
import random
import FastExponentiation
import hashlib
import time
from time import gmtime, strftime

__g__=2
__prime__=10007
__ys__=0
__yn__=0

def Signature(Message):
	global __g__,__ys__,__prime__,
	q=PrimeDivisor.Prime(__prime__-1)
	k1=random.randint(1,q)
	r1=FastExponentiation.SquareAndMultiply(__g__,k1,__prime__)
	hash1=hashlib.sha1()
	hash1.update(Message+str(r1))
	sha_hex=hash1.hexdigest()
	e1=int(sha_hex,16)
	xs=random.randint(0,q-1)
	__ys__=FastExponentiation.SquareAndMultiply(__g__,xs,__prime__)
	s1=(e1*xs+k1)%q
	#WithoutTimestamp(s1,e1,Message);
	TSS(q,s1,e1,Message)

def TSS(q,s1,e1,Message):
	global __g__, __yn__,__prime__
	xn=random.randint(0,q-1)
	__yn__=FastExponentiation.SquareAndMultiply(__g__,xn,__prime__)
	t=strftime("%Y-%m-%d %H:%M:%S", gmtime())
	k2=random.randint(1,q)
	r2=FastExponentiation.SquareAndMultiply(__g__,k2,__prime__)
	sha=hashlib.sha1()
	sha.update(t+str(e1)+str(r2))
	sha_hex=sha.hexdigest()
	e2=int(sha_hex,16)
	s=(k2-e2*(e1*xn+s1))%q
	print s,t,e2,r2
	WithTimestamp(t,s,e2,Message)
	

def WithoutTimestamp(s1,e1,Message):
    global __g__,__yn__,__ys__,__prime__
    q=pow(__ys__,e1,__prime__)
    r1=FastExponentiation.SquareAndMultiply(__g__,s1,__prime__)*pow(q,__prime__-2,__prime__)
    r11=pow(r1,1,__prime__)
    print r11
    hash1=hashlib.sha1()
    hash1.update(Message+str(r11))
    sha_hex=hash1.hexdigest()
    output=int(sha_hex,16)
    print output

def WithTimestamp(t,s,r1,e2,Message):
    global __g__,__prime__,__ys__,__yn__
    hash1=hashlib.sha1()
    hash1.update(Message+str(r1))
    sha_hex=hash1.hexdigest()
    e1=int(sha_hex,16)
    temp=e1*e2
    temp1=pow(__ys__*__yn__,temp,__prime__)
    temp2=pow(__r1__,e2,__prime__)
    out=(pow(__g__,s,__prime__)*temp1*temp2)%__prime__
    hash1=hashlib.sha1()
    hash1.update(t+str(e1)+str(out))
    sha_hex=hash1.hexdigest()
    final=int(sha_hex,16)
    print final

Signature('hanok')