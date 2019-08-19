# _*_ coding ：UTF-8 _*_
# 开发人员   ：52875
# 开发时间   ：2019/6/11 19:44
# 文件名称   ：Test.PY
# 开发工具   ：PyCharm
capital = []
lower_case = []
number = []
for i1 in range(48, 58):
    capital.append(chr(i1))
for i2 in range(65, 91):
    lower_case.append(chr(i2))
for i3 in range(97, 123):
    number.append(chr(i3))
print(capital)
print(lower_case)
print(number)
print(','.join(chr(i4) for i4 in range(48, 58)))
print(','.join(chr(i5) for i5 in range(65, 91)))
print(','.join(chr(i6) for i6 in range(97, 123)))

