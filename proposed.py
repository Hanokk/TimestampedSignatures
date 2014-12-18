import sys
import PrimeDivisor
import random
import FastExponentiation
import ExtendedEuclidean
import hashlib
import time
import timeit
from time import gmtime, strftime

__p__=10193
__q__=10181
__n__=__p__*__q__
totient=(__p__-1)*(__q__-1)
e=PrimeDivisor.Prime(totient-1)
d=ExtendedEuclidean.ExtendedEuclidean(e,totient)

Message="123456789"

def signature(Message):
    global __n__,d
    Message=int(Message)
    u=random.randint(1,__n__-1)
    x=random.randint(1,__n__-1)
    y=FastExponentiation.SquareAndMultiply(2,x,__n__)
    #print y
    s=FastExponentiation.SquareAndMultiply(y,d,__n__)
    digest=(Message*FastExponentiation.SquareAndMultiply(2,u,__n__))%__n__
    r1=(s+digest)%__n__
    TSS(s,r1,u,x,y)

def finalsignature(s,r,r1,r2,t,u,x,y):
    global __n__
    invTemp=FastExponentiation.SquareAndMultiply(x,__n__-2,__n__)
    l=(invTemp*(r2-u+r1))%__n__
    verification(s,y,l,r,t)


def TSS(s,r1,u,x,y):
    t=987654321
    k=random.randint(1,__n__-1)
    r2=(k-r1-t)%__n__
    temp=FastExponentiation.SquareAndMultiply(2,k,__n__)
    r=((r1-s)*(FastExponentiation.SquareAndMultiply(temp,__n__-2,__n__)))%__n__
    finalsignature(s,r,r1,r2,t,u,x,y)

def verification(s,y,l,r,t):
    global e,__n__
    y1=FastExponentiation.SquareAndMultiply(s,e,__n__)
    #print y1
    m=(r*FastExponentiation.SquareAndMultiply(y,l,__n__)*FastExponentiation.SquareAndMultiply(2,t,__n__))%__n__
    print m

signature(Message)