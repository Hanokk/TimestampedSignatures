def MillerRabin(number):
    m=number-1
    __k__=0
    __prime__=1
    __composite__=0
    while m%2==0:
        m=m/2
        __k__+=1
    #print m,__k__
    __T__=pow(2,m,number)
    if __T__==1 or (__T__-number)==-1:
        return __prime__
    
    for i in range(__k__-1):
        __T__=pow(__T__,2,number)
        if (__T__-number)==-1:
            return __prime__
        if __T__==1:
            return __composite__

    return __composite__