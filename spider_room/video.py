#-*- codeing = utf-8 -*-
#@Time : 2020/5/22 20:20
#@Author : dele
#@File : video.py
#@Software: PyCharm


import requests
import pprint

for page in range(0,3):
    print('==============================正在抓取{}页数据======================='.format(page + 1))
    video_url = 'https://v.6.cn/minivideo/getlist.php?act=recommend&page={}&pagesize=20'.format(str(page+1))

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }

    response = requests.get(url= video_url,headers= headers)

    data = response.json()

    # print(data)

    data_list = data['content']['list']
    print(data_list)


    for datalist in data_list:
        video_title = datalist['title'] +'.mp4'
        play_url = datalist['playurl']
        print(video_title,play_url)

        print('srart download.....：', video_title)
        video_data = requests.get(play_url,headers=headers).content

        with open('video\\'+ video_title,mode='wb') as f:
            f.write(video_data)
            print('download finised ....\n')


























