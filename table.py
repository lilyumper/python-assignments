x = range(1, 13)
y = range(1, 13)
for i in x:
    for j in y:
        print "%4d" % (i*j),
        j+=1
    print ""
    i+1 
print "-" * 50   
