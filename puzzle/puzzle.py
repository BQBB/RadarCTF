import re
import requests
c=requests.get('http://blackfoxs.org/radar/puzzle/',headers={'user-agent':'9e9'})
re=re.search('id="desc">(.*?)</h2>',c.text)
result=re.group(1)
print(result)
input()
