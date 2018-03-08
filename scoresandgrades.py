def scores_grades():
    import random  
    for i in range(11):
        num = random.randint(60, 100)
        if num >= 90:
            print "Score:",num," ", "Your Grade is A"
        elif num <= 89 and num >=80:
            print "Score:",num, " ", "Your Grade is B"
        elif num <= 79 and num >=70:
            print "Score:", num, " ", "Your Grade is C"
        elif num <= 69 and num >= 60:
            print "Score:", num, " ", "Your Grade is D"
        elif num <=59:
            print "Score:", num, " ", "Please Study Harder"
scores_grades()
