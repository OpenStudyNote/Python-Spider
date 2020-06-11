#-*- codeing = utf-8 -*-
#@Time : 2020/5/9 20:09
#@Author : dele
#@File : taobao_demo.py
#@Software: PyCharm


# 模块导入
from selenium import webdriver
import time


def search_product(key):
    driver.find_element_by_id('q').send_keys(key)
    driver.find_element_by_class_name('btn-search').click()
    driver.maximize_window()
    time.sleep(15)

def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq"]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        price = div.find_element_by_xpath('.//strong').text +'Y'
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        name = div.find_element_by_xpath('.//div[@class="shop"]/a').text
        print(info,price,deal,name,sep='')


def main():
    search_product(keyword)
    get_product()



if __name__ == '__main__':
    keyword = input('请输入关键字：')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')
    main()

