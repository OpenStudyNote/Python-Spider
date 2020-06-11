import requests  #导入模块 pip install requests
import pprint
for page in range(0,2):   # range(0,n) 表示页数
    print('==============================正在抓取{}页数据======================='.format(page + 1))
    # 1、分析目标网页，确定爬取的url路径，headers参数
    base_url ='https://www.ku6.com/video/feed?pageNo={}&pageSize=40&subjectId=74'.format(page)

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
