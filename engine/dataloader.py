import random

def dataload(gender):
    if gender:
        filename = open('res/male_name.txt', encoding='utf-8')
    else:
        filename = open('res/female_name.txt', encoding='utf-8')
    fs = open('res/surnames.txt',encoding='utf-8')
    namedb= []
    surdb= []
    for line in filename:
        line = line.replace('\n', '')
        namedb.append(line)
    for line in fs:
        line = line.replace('\n', '')
        surdb.append(line)
    nameindex = random.randint(0,len(namedb))
    surindex = random.randint(0,len(surdb))
    print(surdb[surindex]+' '+namedb[nameindex])
    filename.close()
    fs.close()
    return namedb[nameindex], surdb[surindex]
