
username = 'dianna.nikoda@bk.ru'
sep = '@'
rest = username.split(sep, 1)[0]
dot = '.'
year = str(2021-25)[2:]
newstr = dot.join([rest,year])
print(newstr)