import random
fmn = open('res/male_name.txt',encoding='utf-8')
fs = open('res/surnames.txt',encoding='utf-8')
namedb=[]
surdb=[]
for line in fmn:
    line=line.replace('\n','')
    namedb.append(line)
for line in fs:
    line=line.replace('\n','')
    surdb.append(line)
nameindex=random.randint(0,len(namedb))
surindex=random.randint(0,len(surdb))
print(surdb[surindex]+' '+namedb[nameindex])
fmn.close()
fs.close()
