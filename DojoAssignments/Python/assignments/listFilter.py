def function(*x):
    num = 0
    str1 = ''

    for each in (x):
        if type(each) is list:
            for every in (each):
                if type(every) is int:
                    num += every
                if type(every) is str:
                    str1 += (every)
        else:
            if type(each) is int:
                num += each
            if type(each) is str:
                str1 += (each)
    if num != 0 and str1 == '':
        print('this list contains only integers')
        print('sum: ' + str(num))
    elif str1 != '' and num ==0:
        print('this list contains only strings')
        print('String: ' + str1)
    else:
        print('this list is mixed')
        print('Sum: ' + str(num))
        print('String: ' + str1)

function([1,2,3,4], 'hi', 7)
