#replace 118 with { and 90 with _ and 120.102 with }
a='109.92.95.92.109.{.109.92.105.95._.100.110._.105.106.111._.98.106.106.95._.100.95.96.92._.103.106.103.}'
b=a.split('.')
c='abcdefghijklmnopqrstuvwxyz'
d='92.93.94.95.96.97.98.99.100.101.102.103.104.105.106.107.108.109.110.111.112.113.114.115.116.117'
e=d.split('.')
result=''
ff={}
for i in range(0,26):
	ff[str(e[i])]=c[i]
for i in b:
	if i!='{' and i!='}' and i!='_':
		result+=ff[str(i)]
	else:
		result+=i
print(result)
input()
