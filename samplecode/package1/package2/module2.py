print(f'加载 {__file__}')
print(f'此时变量 __name__ 的值是：{__name__}')
a=f'来自 {__file__} 的 a'
_notvisable='可以通过from xxx import * 导入这个变量'
def f():
    print(f"在{f}中，__name__的值是{__name__}")

__all__=['f','_notvisable']
print(f'加载 {__file__} 结束')