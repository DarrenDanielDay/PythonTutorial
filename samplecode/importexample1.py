import package1.package2.module2

print(package1.package2.module2.a)

from package1.module1 import *

try:
    print(a)
    print(_notvisable)                       # 异常，带前置下划线的默认不导入
except Exception as e:
    print(e)

del a
del f

from package1.package2.module2 import *


try:
    print(_notvisable)                       # 正常， __all__中有'_notvisable'
    f()
    print(a)                                 # 异常， __all__中没有'a'
except Exception as e:
    print(e)

import package1.module1

print(f'在这里，__name__的值是 {__name__}')
package1.module1.f()

