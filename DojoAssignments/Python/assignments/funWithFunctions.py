def oddEven(a):
    if a % 2 == 0:
        print("Number is " + str(a) + ". It is an even number")
    else:
        print("Number is " + str(a) + ". It is an odd number")
oddEven(1)
oddEven(12)
oddEven(2000)

def multiply(a, b):
    if type(a) is list:
        for each in range(0, len(a)):
            a[each] *= b
        print(a)
    else:
        print(a * b)

multiply(4, 5)
multiply([1,2,3,4,5], 7)
