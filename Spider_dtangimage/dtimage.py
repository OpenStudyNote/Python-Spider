#-*- codeing = utf-8 -*-
#@Time : 2020/5/17 20:18
#@Author : dele
#@File : dtimage.py
#@Software: PyCharm



# 模块导入
import urllib.parse
import json
import jsonpath
import requests

image_num=0
keyword = '三上悠亚'
kw = urllib.parse.quote(keyword)
print(kw)
for page in range(0,2400,24):

    base_url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'.format(kw,page)

    response = requests.get(base_url)
    html_data =response.text
    # print(html_data)
    html_doc= response.json()
    image_urlpaths =jsonpath.jsonpath(html_doc,"$..path")
    # "$..path" $.. 表示任何位置的（所有位置）path是json格式里面的一个东西，看网页结构是啥子就是啥子，提取数据
    print(image_urlpaths)


    for image_urlpath in image_urlpaths:
        response = requests.get(image_urlpath)
        with open(r'E:\deep learning\Reptile\Spider_dtangimage\mrhua\{}.jpg'.format(image_num),'wb') as f:
            f.write(response.content)
            image_num +=1



