#-*- codeing = utf-8 -*-
#@Time : 2020/5/7 20:21
#@Author : dele
#@File : Spider_yyvideo.py
#@Software: PyCharm

#### 1、分析目标网页，确定爬取的url路径，headers参数
#### 2、发送请求--requests 模拟浏览器发送请求，获取响应数据
#### 3、解析数据 json模块：把json字符串转化成python可交互的数据类型
#### 4、保存数据--保存在目标文件夹中


### 模块导入

import requests
import parsel
import pprint


# 1、分析目标网页，确定爬取的url路径，headers参数
# url地址
page = 0
while True:
    page +=1
    base_url = 'https://api-tinyvideo-web.yy.com/home/tinyvideos'
    params = {'data': '{"uid":0,"page":%s,"pageSize":10}' % str(page)}
    # headers参数
    headers= {'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }

    # 2、发送请求--requests 模拟浏览器发送请求，获取响应数据
    response = requests. get(url=base_url,headers= headers,params=params)
    data = response.json()
    # pprint.pprint(data)# 格式化打印

    # 3、解析数据 json模块：把json字符串转化成python可交互的数据类型

    # data_list = data['data']['response']['videos']#列表

    # 提取字段
    data_list = data['data']['data']
    # print(data_list)
    # 遍历列表
    # 查看json里面的resdesc resurl

    for datalist in data_list:
        try:

            video_title = datalist['resdesc'] +'.mp4'  #视频的文件名
            video_ur1 = datalist['resurl']  # 视频的ur1地址
            print(video_title,video_ur1)
        except Exception as e:
            break


        print('srart download.....：',video_title)
        video_data = requests.get(video_ur1,headers=headers).content
        # 4、保存数据--保存在目标文件夹中
        with open('video\\'+ video_title,mode='wb') as f:
            f.write(video_data)
            print('download finised ....\n')

print('下载结束了')




