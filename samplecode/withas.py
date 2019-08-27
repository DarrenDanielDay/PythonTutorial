class T:
    def __init__(self, x):
        self.x=x
    def __enter__(self):
        print(self.x)
        if isinstance(self.x, int):
            return self
        elif isinstance(self.x, (tuple, list)):
            return self.x 
        else:
            raise ValueError(int)
    def __exit__(self,a,b,c):
        print(self.x,a,b,c)
        return 1

with T((1,2)) as tpl:
    print(tpl)
