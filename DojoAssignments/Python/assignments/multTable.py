str1 = 'x___1___2___3___4___5___6___7___8___9__10__11__12_'
print(str1)
for x in range(1,13):
    str1 = str(x) + '_'
    for y in range(1,13):
        z = x * y
        if z < 10:
            str1 += '__' + str(z) + '_'
        elif z > 10 and z < 100:
            str1 += '_' + str(z) + '_'
        else:
            str1 += str(z) + '_'
    print(str1)
