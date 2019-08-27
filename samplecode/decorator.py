def message(func):
    print(f'{func}的装饰器初始化')
    def w(*args, **kw):
        positional=','.join(str(i) for i in args)
        keyword=','.join(f'{k}={v}' for k, v in kw.items())
        argls=f"{positional}{',' if positional != '' else ''}{keyword}"
        print(f'调用函数 {func.__name__}({argls})')
        rs=func(*args, **kw)
        print(f'调用函数 {func.__name__}({argls}) 结束')
        return rs
    return w

class A:
    def __init__(self,data):
        print(f'对象{self}初始化')
        self.data=data
    @message
    def echo(self):
        print(f'复述{self.data}')

a=A('你好')
a.echo()