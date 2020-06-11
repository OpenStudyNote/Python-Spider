#-*- codeing = utf-8 -*-
#@Time : 2020/5/26 21:09
#@Author : dele
#@File : cosplay_demo.py
#@Software: PyCharm

import  requests
import  parsel
import  os
# 循环抓取

for page in range(1,6):
    base_url = 'http://www.win4000.com/meinvtag26_{}.html'.format(str(page))

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    # 发送请求--requests 模拟浏览器发送请求，获取响应数据
    response = requests.get(url=base_url, headers=headers)
    response.encoding = response.apparent_encoding  # 自动识别编码格式  “charset=utf-8"  ”utf-8“
    data_text = response.text

    # print(data_text) #打印网页源代码

    html_data = parsel.Selector(data_text)
    data_list = html_data.xpath('//div[@class="Left_bar"]//ul/li/a/@href').extract()
    # print(data_list)

    for alllist in data_list:
        response_2 = requests.get(url=alllist, headers=headers).text
        response_2_data = parsel.Selector(response_2)
        img_url = response_2_data.xpath('//div[@class="pic-meinv"]/a/img/@data-original').extract_first()

        # print(img_url) 打印每一个图片链接地址

        img_url_data = requests.get(url=img_url, headers=headers).content

        file_name = img_url.split('/')[-1]
        # 二进制保存数据
        with open('cosplay_img\\' + file_name, mode='wb') as f:
            print('正在保存图片：', file_name)
            f.write(img_url_data)