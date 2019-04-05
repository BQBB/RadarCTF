import re
import base64
g=open('flag.txt','r')
g=g.readlines()
ii=0
result=''
for i in g:
    i=i.strip('\n')
    result+=i[ii]
    ii+=1
flag=base64.b64decode(result+'=').decode('utf-8')
print(flag)
input()
