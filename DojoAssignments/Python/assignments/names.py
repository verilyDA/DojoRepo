students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names( myDict):
    str1 = ''
    for each in myDict:
        for item in each:
            str1 += str(each[item])+' '
        print (str1)
        str1 = ''

#names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def newNames(myDict):
    str1 = ''
    count = 0
    nameCount = 0
    for item in myDict:
        print(item)
        for each in myDict[item]:
            count += 1
            str1 += str(count) + ' - '
            for thing in each:
                str1 += str(each[thing])+' '
                nameCount += len(each[thing])
            str1 += '- ' + str(nameCount)
            print (str1)
            str1 = ''
            nameCount = 0
        count = 0

newNames(users)
