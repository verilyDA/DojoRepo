import random
random_num = random.random() * 100 + 1
random_arr = []
for each in range(0,10):
    random_arr.append(random.random() * 100 + 1)

def scoresNgrades(a):
    print("Scores and Grades")
    if type(a) is list:
        for each in range(0, len(a)):
            if a[each] > 59 and a[each] <= 69:
                print("Score: " + str(a[each]) + "; Your grade is D")
            elif a[each] > 69 and a[each] <= 79:
                print("Score: " + str(a[each]) + "; Your grade is C")
            elif a[each] > 79 and a[each] <= 89:
                print("Score: " + str(a[each]) + "; Your grade is B")
            elif a[each] > 89:
                print("Score: " + str(a[each]) + "; Your grade is A")
            else:
                print("Score: " + str(a[each]) + "; Your grade is not very good")
    else:
        if a > 59 and a <= 69:
            print("Score: " + str(a) + "; Your grade is D")
        elif a > 69 and a <= 79:
            print("Score: " + str(a) + "; Your grade is C")
        elif a > 79 and a <= 89:
            print("Score: " + str(a) + "; Your grade is B")
        elif a > 89:
            print("Score: " + str(a) + "; Your grade is A")
        else:
            print("Score: " + str(a) + "; Your grade is not very good")
    print("End of program. Bye!")

scoresNgrades(random_num)

scoresNgrades(random_arr)
