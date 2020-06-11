#-*- codeing = utf-8 -*-
#@Time : 2020/5/8 20:09
#@Author : dele
#@File : company.py
#@Software: PyCharm

# 模块导入

from urllib.parse import urlencode
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd


# 1.网页源代码提取
def get_web_page(i):
    try:
        headers = {'user-agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
                   }

        paras ={
            'reportTime':'2020-03-31',
            'pageNum':i
        }
        base_url = 'https://s.askci.com/stock/a/?' + urlencode(paras)
        # print(base_url)
        response= requests.get(url=base_url,headers =headers)
        if response.status_code == 200 :
            return response.text # 网页源代码文本

    except requests.exceptions.RequestException:
        print("爬取失败")




# 2.提取网页数据
def parse_one_page(html):
    # # 解析
    # soup = BeautifulSoup(html)
    # tr_list = soup.find_all('tbody')
    # print(tr_list)
    # for data in tr_list:
    #     sub_data= data.text.split()
    #     print(sub_data)
    tb1 = pd.read_html(html,header= 0)[3]
    # print(tb1)
    return tb1

# 3.保存网页数据
def save_csv(data):
    df = pd.concat(data)
    df.to_csv(r'E:\deep learning\Reptile\Spider_company\company.csv',index = False)



# 4.简单数据可视化

def main(page):
    data =[]
    for i in range(1,page+1):
        web_data = get_web_page(i)
        tb= parse_one_page(web_data)
        data.append(tb)
    save_csv(data)

#
if __name__ == '__main__':
    main(10)


