dct={'a':111,'b':'BBB','c':["ccc"]}
ls=[*range(3)]

def none_kw(p1,p2='dft',*args):
    print(p1,p2,args)


def general(p1,p2='dft',*args,**kw):
    print(p1,p2,args,kw)

def dftfst(p1,p2=1,*args,behind):
    print(p1,p2,args,behind)

def f1(a,b=1,*args,k1,k2=1,k3,**kw):       # 正确
    print(a,b,args,k1,k2,k3,kw)

def fff(**kw):
    pass

def t1():
    none_kw(a=0,*(),**{'p2':2},aa=1)

def t2():
    general(*ls)

def t3():
    dftfst(1,2,3,4,5,6,behind='hello')

def t4():
    f1(*(1,2,3,4,5),k1=6,**{'k3':-1})

def t5():
    f1(**{'a':0,'k1':9,'k3':-1})

ts=[t1,t2,t3,t4,t5]

for t in ts:
    try:
        t()
    except Exception as e:
        print(e)