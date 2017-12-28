# find and replace
str1 = "It's thanksgiving day. It's my birthday, too!"
print(str1.find('day'))#print needs parentheses apparently
str2 = str1.replace("day","month")
print(str2)

#min and max
x = [2,54,-2,7,12,98]
print(min(x))
print(max(x))

#first and last
x = ['hello',2,54,-2,7,12,98,'world']
print(x[0])
print(x[len(x)-1])

#new lists
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = []
x.sort()
count = 0
end = (len(x) - 1 ) / 2
while count < end:
    y.append(x[count])
    count += 1
count = 0
while count < end:
    x.pop(0)
    count += 1
x.insert(0, y)
print(x)
