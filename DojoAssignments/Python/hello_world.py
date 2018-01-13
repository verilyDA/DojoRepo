print "hello World!"
x = 42
y = "hello"
print x
print y
# indicates a comment
'''
this allows for multi
line
comments to be blacked out
'''
'''
primitive data types:
boolean
numbers
strings
Composite types:
tuples - cant be modded after creation and can hold a group of values, can contain mixed data types
lists - is an array
dictionaries - group of key-value pairs
'''
#for loops
#for (variable) in (range[start, finish])||(sequence or list):
for count in range(0,5):
    print count
    #output would be 0, 1, 2, 3, 4

list = [2, 4, 'dog', 99, ['list', 'inside']]
for element in list:
    print element
    #output would be 2, 4, 'dog', 99, ['list', 'inside']

#while loops
#declare variable
count = 0
while count < 5:
    print count
    count += 1 #needs an increment or decrement else stuck in an infinite loop

#breaks
for val in 'string':
    if val == 'i':
        break
    print val
#output would be s, t, r with the break being at i and stopping the loop

#continue
for val in 'string':
    if val == 'i':
        continue
    print val
#output s,t,r,n,g continue basically skips that iteration of the loop

#pass
#useful in places where you want the code to 'pass' over this block, kind of like a place holder for later code

#else
x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print 'final else statement'
# useful when the loop runs its course but you'd like something to happen after it finishes


i,j = 1,2,3
