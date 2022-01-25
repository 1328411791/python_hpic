import string
import time

import requests
import re
cookie = "pwd=123"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    ,"cookie":cookie # 使用cookie
}
response = requests.get('http://cz.zhaowho.cn:68/qq.php?t=164302547429506&gs=tar18&_wv=vmsl&alert%28%29id=1807139605#alert%28%29',headers=headers)
list_url=re.findall(r"<img src=\"(.*?)\"",response.text)
num=len(list_url)-3
print(list_url)
for i in range(num):
    response=requests.get(list_url[i])
    with open(str(i)+".jpg","wb+") as f:
        f.write(response.content)
print(list_url)
print("Finish")