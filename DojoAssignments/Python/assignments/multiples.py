'''
multiples
write code that prints all numbers from 1 to 1000. use a for loop
Create another program that prints all the multiples of 5 from 5 to 1,000,000.
'''
'''
for count in range(1, 1000):
    if count % 2 == 1:
        print(count)

for count in range(5, 1000000):
    if count % 5 == 0:
        print(count)
'''

#sum lists
a = [1, 2, 5, 10, 255, 3]
res = 0
for count in a:
    res += count
print(res)

#average lists
res = 0
for count in a:
    res += count
res /= len(a)
print(res)
