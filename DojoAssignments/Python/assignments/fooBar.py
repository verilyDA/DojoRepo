for x in range(100, 100000):
    count = 0
    foo = 0
    bar = 0
    for y in range(1,x):
        if y * y == x:#squares
            print('bar: ' + str(x))
            foo = 1
        if x % y == 0:
            count += 1
    if count == 1:
        print('foo: ' + str(x))
        foo = 1
    elif foo == 0 and bar == 0:
        print('foobar: ' + str(x))
    bar = 0
    foo = 0
