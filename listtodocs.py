name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas","nobody likes monkeys"]

def zipit(list1,list2):
    newlist = zip(list1,list2)
    print newlist
    newerlist = dict(newlist)
    print newerlist
zipit(name,favorite_animal)

# def testing(list1,list2):
#     if len(list2) > len(list1):
#         zip(list2,list1)
#     else:
#         zip(list1,list2)
