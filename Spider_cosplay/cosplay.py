#-*- codeing = utf-8 -*-
#@Time : 2020/5/26 20:17
#@Author : dele
#@File : cosplay.py
#@Software: PyCharm

#爬虫的般思路
#1、分析目标网页。确定爬取的ur1路径，headers参数
#2、发送请求--requests 模拟浏览器发送请求，获取响应数据
#3、解析数据--parsel转化为Selector对象，Selector对象 具有xpath的方法，能够对转化的数据进行处理
#4、保存数据


# cosplay 静态网页 数据获取 基本方法


# 模块导入
import  requests
import  parsel
import  os

# 目标网页分析

base_url = 'http://www.win4000.com/meinvtag26.html'

headers ={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
# 发送请求--requests 模拟浏览器发送请求，获取响应数据
response = requests.get(url=base_url,headers= headers)
response.encoding = response.apparent_encoding # 自动识别编码格式  “charset=utf-8"  ”utf-8“
data_text = response.text

# print(data_text) #打印网页源代码

html_data= parsel.Selector(data_text)
data_list = html_data.xpath('//div[@class="Left_bar"]//ul/li/a/@href').extract()
print(data_list)

for alllist in data_list:
    response_2 =requests.get(url=alllist,headers=headers).text
    response_2_data = parsel.Selector(response_2)
    img_url = response_2_data.xpath('//div[@class="pic-meinv"]/a/img/@data-original').extract_first()

    print(img_url)


    img_url_data = requests.get(url=img_url,headers=headers).content

    file_name = img_url.split('/')[-1]

    with open('cosplay_img\\'+file_name,mode='wb') as f:
        print('正在保存图片：',file_name)
        f.write(img_url_data)








