def function( x, y):
    if x == y:
        print('the lists are the same')
    else:
        print('the lists are not the same')

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

function( list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

function( list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

function( list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

function( list_one, list_two)
