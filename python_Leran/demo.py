#-*- codeing = utf-8 -*-
#@Time : 2020/5/4 7:47
#@Author : dele
#@File : demo.py
#@Software: PyCharm

d={"大海":"蓝色","天空":"灰色","大地":"黑色"}
print(d["大地"],d.get("太空","蓝色"))

dict = {'Name': 'Xiaoxiao', 'Age': 18, 'School': 'Hrbeu'}

print (dict.get('School'))
print (dict.get('Sex', "Nothing"))
print(dict.get('Age'))