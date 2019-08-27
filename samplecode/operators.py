from functools import wraps

def show(func):
    @wraps(func)
    def shower(*args,**kw):
        print(func.__name__)
        return func(*args,**kw)
    return shower

class LR:
    def __init__(self,x):
        self.x=x

    @show
    def __pos__(self):
        return self

    @show
    def __add__(self,other):
        if isinstance(other,LR):
            return self.x+other.x
        return self.x+other

    @show
    def __radd__(self,other):
        if isinstance(other,LR):
            return self.x+other.x
        return self.x+other

l=LR(2)
r=LR(3)

print(l+1)
print(1+r)
print(l+r)
print(+r)