import random
f = open('res/male_name.txt',encoding='utf-8')
namedb=[]
for line in f:
    line=line.replace('\n','')
    namedb.append(line)
nameindex=random.randint(0,len(namedb))
print(str(nameindex+1)+' '+namedb[nameindex])
f.close()
