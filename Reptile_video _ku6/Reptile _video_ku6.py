# 学习模块
# requests
# json
# 动态数据抓包

# 爬虫的一般思路
# 1、分析目标网页，确定爬取的url路径，headers参数
# 2、发送请求 requests 模拟浏览器发送请求，获取响应数据
# 3、解析数据 json模块：把json字符串转化成python可交互的数据类型
# 4、保存数据 保存在目标文件夹中

import requests  #导入模块 pip install requests
import pprint

# 1、分析目标网页，确定爬取的url路径，headers参数
base_url ='https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=74'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 2、发送请求 requests 模拟浏览器发送请求，获取响应数据
response = requests.get(base_url,headers= headers) #
data = response.json()
print(data)

# 3、解析数据 json模块：把json字符串转化成python可交互的数据类型

data_list = data['data']
# print.pprint(data_list) 打印列表

# for循环遍历列表
for datal in data_list:
    video_title = datal['title'] + ".mp4"  # 视频标题
    video_url = datal['playUrl']           #  视频Url
    # print(video_title,video_url)           # 打印标题
    print('srart download.....：',video_title)  # 打印 srart download  视频标题
    video_data = requests.get(video_url,headers=headers).content  #
    # 图片视频音频文件都是二进制的，用wb进行保存，写入response.content content方法
    with open('video\\'+ video_title,mode='wb') as f:  #保存数据
        f.write(video_data)
        print('download finised ....\n')

print('download endding')
