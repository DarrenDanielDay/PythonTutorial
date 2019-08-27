def message1(s):
    print(f'\n{s} 之前\n')

def message2(s):
    print(f'\n{s} 之后\n')


message1('import package1')
import package1
message2('import package1')

print('package1变量中有成员：',dir(package1))

message1('import package1.package2')
import package1.package2
message2('import package1.package2')

print('package1变量中有成员：',dir(package1))
