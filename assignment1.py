words = "It's thanksgiving day. It's my birthday, too"
print(words.find('day'))
print words.replace('day', 'today') 

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0:1]
print y[7:]

first = y[0:1]
last = y[7:]
print first + last

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
half1 = [-3,-2,2,6,7]
half2 = [10,12,19,32,54,98]
half2.insert(0,half1)
print half2