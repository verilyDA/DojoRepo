def draw_stars(arr):
    str1 = ""
    for each in arr:
        if type(each) is str:
            for item in range(0, len(each)):
                str1 += each[:1]
        else:
            for item in range(0,each):
                str1 += "*"
        print(str1)
        str1 = ""
draw_stars([1,2,3, 'bob', 'timothy', 'lucas'])
