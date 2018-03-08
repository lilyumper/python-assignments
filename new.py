words = ['hello','world', 'my', 'name', 'is', 'Tom']
char = 'o'
newList =[]

for item in words:
 if item.count(char) !=0:
    newList.append(item)
print newList