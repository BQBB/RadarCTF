flag='4:11:14:11:4:0:8:26:14:3:22:13:9:15:13:27:11:19:3:13:12:27:11:20:20:13:23:4:6:10:5:9:4:28:'
pattern='{qwertyuiopas_dfghjklzxcvbnm}'
re=flag.split(':')
result=''

for i in re:
    if i != '':
        x=pattern[int(i)]
        result+=x
print(result)
input()

