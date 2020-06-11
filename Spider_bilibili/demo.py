#-*- codeing = utf-8 -*-
#@Time : 2020/5/23 21:28
#@Author : dele
#@File : demo.py
#@Software: PyCharm



import requests
import re
for page in range(0,111,10):
    print('==============================正在抓取{}页数据======================='.format(page))
    base_url = 'https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={}&tag=%E5%B0%8F%E8%A7%86%E9%A2%91&type=tag_general_week&platform=pc'.format(page)

    headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }

    response = requests.get(url=base_url,headers=headers)

    data = response.json()

    #print(data)

    data_list = data['data']['items']

    #print(data_list)

    for datalist in data_list:
        video_title = datalist['item']['description'] # 正则
        video_title = re.sub("[\n. /]","-",video_title)
        video_url   = datalist['item']['video_playurl']
        print(video_title,video_url)
        video_data = requests.get(url=video_url, headers=headers).content
        with open("video\\"+video_title+".mp4","wb") as f:
            f.write(video_data)
            print('download finished ....\n')


print('download endding')










