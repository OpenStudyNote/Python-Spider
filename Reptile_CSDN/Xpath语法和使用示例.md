#Xpath语法和使用示例
### Xpath语法

Xpath是一门在XML文档中查找信息的语言，可以用来在XML文档中元素和属性进行遍历，是W3C XSLT标准的主要元素

#####     1，节点关系

父节点，下面例子中，body是h1元素的父节点，h1是body节点的子节点，子节点可以有零个和多个

```html
&lt;body&gt;
     &lt;h1&gt;小白&lt;/h1&gt;
     &lt;h2&gt;小黑&lt;/h2&gt;
&lt;/body&gt;
```

同胞节点：上面例子中，h1和h2就是同胞节点，同胞节点拥有相同父节

**    ****2，节点的选择**

节点是通过路径或者step来选取的，如下表所示

<img src="https://img-blog.csdn.net/20180405162200581?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JvbmdEYW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""><br>

#####     3，使用的技巧

    在一般的爬虫实战中，Xpath路径可以通过谷歌浏览器或火狐浏览器中复制得到，如下图

<img src="https://img-blog.csdn.net/20180405162528200?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JvbmdEYW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""><br>

但是对于新手可以多多尝试自己写Xpath路径，因为有时候复制获取的Xpath路径过长，自己写的可能更简洁些

例子：

```
# //*[@id="qiushi_tag_120129862"]/div[1]/a[2]/h2
# 通过代码即可得到用户id：
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
url = 'http://www.qiushibaike.com/text/'
res = requests.get(url,headers=headers)
selector = etree.HTML(res.text)
id = selector.xpath('//*[@id="qiushi_tag_118732380"]/div[1]/a[2]/h2/text()')
print(id)

# 注意：通过/text()可以获取标签中的文字信息。
# 结果为：
# ["姑苏云琪"]
```

几种解析方式的性能对比

### 综合示例（一）——爬取豆瓣图书TOP250（ 数据存储到CSV）

在以前的例子中，爬取的数据要么直接输出到屏幕，要么就存储到txt文档中，这些格式不利于数据的存储，数据显示的比较乱，所以这里用CSV格式存储数据，且CSV是存储表格数据的常用文件格式，Excel和很多应用都支持CSV格式

<br>

（1）要爬取的内容为豆瓣图书top250的信息，如下图所示

<img src="https://img-blog.csdn.net/20180405164918260" alt=""><br>

（2）通过浏览所知，共10页，每页25本书本信息，前4页的网址如下

https://book.douban.com/top250?start=0<br>

https://book.douban.com/top250?start=25<br>

https://book.douban.com/top250?start=50<br>

https://book.douban.com/top250?start=75<br>

所以只需要更改start=后面的数据就可以构造10页的网址

（3）需要爬取的信息有：书名，书本的链接，作者，出版社，出版日期，评分和评价

（4）运用Python中的CSV库，爬取的学习存储在本地的CSV文本中

<br>

具体的代码如下：

```
# -*- encoding:utf8 -*-
# 爬取豆瓣图书TOP250,爬取的数据存储到CSV文件中
from lxml import etree
import requests
import csv
# wt是python中以文本写 的方式打开,只能写文件,如果文件不存在则创建该文件
fp = open("douban_top250.csv","w")
writer = csv.writer(fp)
# 上面的代码是传教CSV文件,下面是给CSV文件写入表头信息,相当于每一列的列名
writer.writerow(('name', 'url',  'author', 'publisher', 'date', 'price', 'rate', 'comment'))
# 创建url,range的第三个参数是步长
urls = ["https://book.douban.com/top250?start={}".format(i) for i in range(0,250,25)]
# 请求头,用来模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# res = requests.get("http://www.baidu.com",headers=headers)
# # lxml库的etree解析html
# selector = etree.HTML(res.text)
# print type(selector)
for url in urls:
    res = requests.get(url,headers=headers)
    # lxml库的etree解析html
    selector = etree.HTML(res.text)
    # 获取的是一页中所有的书本信息,每本的所有信息都在类为item的tr下面
    infos = selector.xpath("//tr[@class='item']")
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        # 获取的是书本的基本信息,有作者和出版社,和出版日期...
        book_infos = info.xpath('td/p/text()')[0]
        # 作者
        author = book_infos.split('/')[0]
        # 出版社
        publisher = book_infos.split('/')[-3]
        # 出版日期
        date = book_infos.split('/')[-2]
        # 价格
        price = book_infos.split('/')[-1]
        # 书本的评分
        rate = info.xpath('td/div/span[2]/text()')[0]
        # 下面的评论
        comments = info.xpath('td/p/span/text()')
        # 这里单行的if语句是:如果comments的长度不为0时,则把comments的第1个元素给comment,否则就把"空"赋值给comment
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow((name.encode("utf-8"), url.encode("utf-8"), author.encode("utf-8"), publisher.encode("utf-8"), date.encode("utf-8"), price.encode("utf-8"), rate.encode("utf-8"), comment.encode("utf-8")))
# 关闭
fp.close()
```

有个问题是我不知道在哪儿更改写入的编码格式，所以就在最后的写入中，给每个写入的字符串指定字符为“utf-8”这样显的代码显的十分臃肿，去网上查找了几种方式也没有找到答案，

第二个问题是，在写入到最后的时候会提示报错，报一个这样的错误，有点莫名其妙，导致只写入了到大概155条数据

'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)

写入一部分的结果如下，还有一个事，就是写入的csv文件用excel打开会有乱码，所有可以用记事本打开csv文件，然后另存为时，选择右下角的编码格式为“utf-8”这样用excel打开就不会是乱码了

<img src="https://img-blog.csdn.net/20180405190912786" alt=""><br>

<br>

### 数据存储到excel中

使用python的第三方库xlwt，可以将数据写入到excel中，通过 pip install xlwt安装

<img src="https://img-blog.csdn.net/20180406104311511" alt=""><br>

通过下列代码可以将数据写入到excel中：

```
# 导入写入excel的库文件
import xlwt
# 创建工作簿，并指定编码格式，默认编码格式为ascii
book = xlwt.Workbook(encoding="utf-8")
# 创建工作表
sheet = book.add_sheet("sheet1")
# 在相应单元格写入数据，前面的（1,1）在第二行第二列写入小白
sheet.write(1,1,"小白")
# 保存到文件
book.save("test.xls")
```

具体的结果如下，在第二行第二列写入了小白

<img src="https://img-blog.csdn.net/20180406105211736" alt=""><br>

<br>

### 综合示例（二）——爬取起点中文网小说信息

如下图所示<img src="https://img-blog.csdn.net/20180406110130260" alt="">

第一页的网址如下所示：

https://www.qidian.com/all?orderId=&amp;style=1&amp;pageSize=20&amp;siteid=1&amp;pubflag=0&amp;hiddenField=0&amp;page=1<br>

感觉有点长，点击下一页跳转，只有最后的page=后面的数字有变化，而前面中间的一段的字感觉就是控制分类的，所有经过一点点的删除，发现

https://www.qidian.com/all? &amp;pageSize=20&amp;siteid=1&amp;pubflag=0&amp;hiddenField=0&amp;page=1

https://www.qidian.com/all? &amp;pubflag=0&amp;hiddenField=0&amp;page=1

https://www.qidian.com/all? page=1

上面网址所跳转的都是第一页的书本信息，所有只需要变化最后的page页数就可以访问后面的一系列的信息（因缺思厅）

（2）需要爬取的信息有：小说名，作者，小说类型，完成情况，介绍和字数

<img src="https://img-blog.csdn.net/20180406111116223" alt=""><br>

具体的实现如下，有一个问题就是，小说的字数获取不了，在源代码上显示的是一些框，可能是动态显示的，也不知道该如何获取，暂时就这样吧，写入到excel中还比较简单理解的。

```
# -*- encoding:utf8 -*-
# 爬取起点中文网小说信息，存储到excel表中
import requests
import xlwt,time
from lxml import etree
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# 初始化列表，用来存入爬虫数据
all_info_list = []
# 定义获取爬虫信息的函数
def get_info(url):
    res = requests.get(url,headers=headers)
    selector = etree.HTML(res.text)
    # 先找到包含所有书本信息的标签，依次循环
    infos = selector.xpath("//ul[@class='all-img-list cf']/li")
    for info in infos:
        # 书名
        title = info.xpath("div[2]/h4/a/text()")[0]
        # 作者
        author = info.xpath("div[2]/p[1]/a[1]/text()")[0]
        # 类型
        style1 = info.xpath("div[2]/p[1]/a[2]/text()")[0]
        style2 = info.xpath("div[2]/p[1]/a[3]/text()")[0]
        style = style1+" &amp; "+style2
        print style
        # 状态,连载还是完结
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        # 书本的介绍
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        # # 字数获取不到，算了
        # word = info.xpath('div[2]/p[3]/span/text()')[0]
        # print word
        # 每一本书的信息
        info_list = [title, author, style, complete, introduce]
        # 把每本书的信息拼接到总的列表中
        all_info_list.append(info_list)
    time.sleep(1)
    pass
# get_info("https://www.qidian.com/all?page=1")

# 程序入口
if __name__=="__main__":
    # 创建要爬取的链接
    urls = ["https://www.qidian.com/all?page={}".format(i) for i in range(1,500)]
    for url in urls:
        get_info(url)
    # header = ['title', 'author', 'style', 'complete', 'introduce']
    header = ["书名","作者","风格","状态","介绍"]
    # 创建工作簿
    book = xlwt.Workbook(encoding="utf-8")
    # 在工作簿中创建工作表
    sheet = book.add_sheet("Sheet1")
    for i in range(len(header)):
        # 循环写入每一列的标题，从第一列开始
        sheet.write(0,i,header[i])
    i = 1# i=1，表示从第二行开始，第一行已经有列的标题了
    for list in all_info_list:
        j = 0
        # all_info_list的每个元素都是一个列表，列表里面都是我们所爬取的数据
        for data in list:
            sheet.write(i,j,data)
            j += 1
        i += 1
    book.save("xiaoshuo.xls")
    pass
```

部分结果如下图所示：

<img src="https://img-blog.csdn.net/20180406150312279" alt=""><br>

还有一个，网页有好几千页，爬取的话，爬个百来页就行了，不然时间太长，我爬取了499页的数据时间有点长了
