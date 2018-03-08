def draw_stars(arr):
    for x in arr:
        stars =""
        if type(x) == int:
            for i in range(0,x):
                stars+= "*"
        elif type(x) == str:
            for i in range(len(x)):
                char =x[0]
                stars += x[0]
        print stars
draw_stars([2,"tom","bobby",6])