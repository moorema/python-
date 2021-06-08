import requests

url = 'https://www.sogou.com/web?query=周杰伦'
dic = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.3'
}
resp = requests.get(url, headers=dic)

print(resp.text)
------------------------------------------------------------------------------------------------------


# 河南采购,cookie手动反反爬(半成品手动cookie会过期)
import requests

url = "http://www.hngp.gov.cn/henan/search?&"
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.3',

}
dc = input('请输入查询的关键字: ')
kw = {
    'ctk': 'eaa01c88ee244aee9f49abd4892654f1',
    "q": dc,
}
cookie = {
    'sId': 'eaa01c88ee244aee9f49abd4892654f1'
}
resp = requests.get(url=url, headers=ua, params=kw, cookies=cookie)
print(resp.text)
resp.close()
------------------------------------------------------------------------------------------------------


# 正则表达式
import re

# findall:匹配所有符合正则的内容
lst = re.findall(r"\w+", "我的电环号码是:10086, 我女朋友的电话号码是10000")
print(lst)

# finditer: 匹配字符串中所哟有的内容,返回的迭代器
it = re.finditer(r"\d+", "我的电环号码是:10086, 我女朋友的电话号码是10000")
for i in it:
    print(i.group())
    
    
------------------------------------------------------------------------------------------------------

s = """
<div class='jay'><span id='1'>法师</span></div>
<div class='jj'><span id='2'>送医</span></div>
<div class='jolin'><span id='3'>张三</span></div>
<div class='sylar'><span id='4'>李四</span></div>
<div class='tory'><span id='5'>王五</span></div>
"""
# (?P<分组名字>正则) 可以单独冲正则内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S) # re.S让点匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("name"))
    print(it.group("id"))

    
 ------------------------------------------------------------------------------------------------------
   
    
#  正则爬取豆瓣250解析数据放到csv文件里
url = "https://movie.douban.com/top250"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.3'
}
resp = requests.get(url, headers=headers)
pageContent = resp.text

# 正则解析数据
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
result = obj.finditer(pageContent)
for it in result:
#    print(it.group("name"))
    dic = it.groupdict()
    csvwriter.writerow(dic.values())

f.close()
print("over!")


------------------------------------------------------------------------------------------------------



