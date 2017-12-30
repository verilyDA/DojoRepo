def fun(words, char):
    newList = []
    for each in words:
        if char not in each:
            continue
        newList.append(each)
    print(newList)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'


fun(word_list, char)
