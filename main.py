import string
import time

import requests
import re
string = "pwd=123"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    ,"cookie":string # 使用cookie
}
 # 这里range(10)可以理解为从0循环到9，下载10张图。这个数字可以随便改
response = requests.get('http://cz.zhaowho.cn:68/qq.php?t=164302547429506&gs=tar18&_wv=vmsl&alert%28%29id=1807139605#alert%28%29',headers=headers) # 每次下载图片
list_url=re.findall(r"<img src=\"(.*?)\"",response.text)
num=len(list_url)-3
print(list_url)
for i in range(num):
    response=requests.get(list_url[i])
    with open(str(i)+".jpg","wb+") as f: # str(i)+'.jpg'是字符串拼接。每次写入一个新的文件。
        f.write(response.content)
print(list_url)
print("Finish")