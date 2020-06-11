#-*- codeing = utf-8 -*-
#@Time : 2020/5/15 20:16
#@Author : dele
#@File : wyyun_music.py
#@Software: PyCharm

import requests
import json

# 搜索url
base_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
# headers 参数 模拟浏览器登录
headers ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

# 修改From data 信息 获取其他歌曲
# data={
#     'params':'y29eUI9upnFLMNmqw2jCYRkbKBXfnYfh0fJ+FJh3xitnR+A5EDGWwPJfWFyNz7imbE+VmDWyO1VfJAEBgpcN3mJUv9YvxvhLv0DwBGf/EBEVpeZnBNTVf+3V7xxtyxYQsye9HLTNZGPTSWsC4WfRZcc5gzB2GdUS3huF2+j2pkBRTf9VSEPsD27oQSU4Z4IJojLz/s9s5tLWIL32E0/dzosOAn6XY+QJABRtByuaf8HR9amZlYOTXn++DPMx35QjVj/dTkIoRQD1T3rSDlhCdFyjMRcnrN+Dq/s8CbSdGak=',
#     'encSecKey':'36f7389ba3af32613955f42e2c8e5bac688c21f59796e8738ba1235a1a56c2656eb3315113c6f39cf6bba5a3ea58fd38d7ac29b8bfb94fb6a49210a3529b04f9c053d26be25ad19cb378c19e28f4fc830fbbad41451240afcf5c6511d3cc5f24ab1799534375d820117a53da7716915889743a133aadf0200fdad2f437b8dc17'
# }
# data ={
#     'params':'ZtkfjPE0FbvosyB4FvRoOwW62auIGyi/tBomCuf6Zh4q55OsLyRV7qOmoG9B6FH1xLYv18l8LlZNPTkIEQ5Iu8kmpe+6KYwilv6xgCHf78ClEQoC6J/L5g9uXD8Hg6lrOtUQIdCXBrOe5ubxrbHR2HqgLNm7i56QU/JNBKSc2sR2AV/BV1r9rqbpATlUUlTOI/i2bYC40pZGNMhgVUJ+tmd0pcM8b0Jbq2wsZem0nl2GTo4vcd4jerjCSXoQrkU/mxwxFF+TyHepgtKef3Ik8Ezwx+NK3rB0fTpFJyKTw8s=',
#     'encSecKey':'ae7e844e01b4a58907b92e8f71e222c5a8f85160ce7bf68ba47b8a8ff181616f0cc955397bbc907ec062ee6a695c6de26ac5629ba933638dcb84f6cb07e1afcdf24db955e22744e3cca3d0c5c18ee27898fc5a2b09a3cfac255a231388cce9da41d3115a67bab703cc377146006525f8eadb953f90e378a6d8b0126c4cdfb376'
# }

data = {

    'params':'4QI0slEwUH5LX0RyN2EG7oxcYxzdfdDC/lCvSlay0zFpOTD7YcyjOuEechTIKXtANulZEXeIhLvuvy6t35zdbFePvHNfgyDYOzB6Dp4cT6SLwoM8mdiab5PU+LFWR5WQgWywQ0bHzPBu05lpNB1qyGBZj8RIDlSohNDAKycc8YlYri0mHjsTs0OsTdPWAXNcJm1FpDZkDLnoT59mAcDUeN6f+jfM0kylGKD4bxQn3JaSpVOiWRTJKLl1tH1K3LsUAXqFv++8xoIgx2Vxpqwg4hxm6b9U3QrdoKJZyWUELvax2Y79iAOpYO5Zkw1d2n8p',
    'encSecKey':'8923fdfa47b7676969b1972b78fe8e7b7349a5fe1bf29480d0d65a1bd31b5d3aff1bc1f2f07343cae56591c823e67e09506d2c98582643542ad4a4230743ee15cf3394fa85ac68edbfce8bac8a1f573d5588e96994cbb696bd1db962ba41ad08e8064b3130033f54897e0c7d275fd509daf133c275d5b637795738ea036401b0'
}

# response requests.post 请求
response = requests.post(url=base_url,headers=headers,data=data).json()
# 获取id_list 列表里面的东西，例如result songs
# 从songs 获得id 下载歌曲，name歌曲名称
id_list = response['result']['songs']
# print(id_list)
# 循环遍历 打印歌曲id name
for idlist in id_list:
    songid = idlist['id']
    name = idlist['name']
    print(songid,name)

    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songid) # vip接口网站
    song_data = requests.get(url=song_url,headers=headers).content
    # print(song_data)
    # 保存MP3文件，二进制保存 'kingGnu/' 文件夹地址
    with open('kingGnu/' +name + '.mp3',"wb") as f:
        f.write(song_data)
        print('download 完成',name)

