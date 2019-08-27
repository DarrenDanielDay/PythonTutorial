import re

rex=r"(\w+)@(\w+(\.\w+)+)"
compile_object=re.compile(rex)  # 这样就得到了编译对象compile_object

target1="someone@example.com"
target2="someone@notcorrect"
match_object1=compile_object.match(target1) # 匹配成功
match_object2=compile_object.match(target2) # 匹配失败，match_object2是None

name=match_object1.group(1)
host=match_object2.group(2)
print(f"用户名：{name}")
print(f"主机域名：{host}")