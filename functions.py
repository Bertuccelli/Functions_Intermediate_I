from socket import SOMAXCONN


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# update values pt1
x[1][0] = 15
print(x)
# update values pt2
students[0]['last_name']='Bryant'
print(students)
# update values pt3
sports_directory['soccer'][0]='Andres'
print(sports_directory)
# update values pt4
z[0]['y']=30
print(z)

# iterate through a list of dictionaries

rollCall = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(element):
    for x in range(0, len(rollCall)):
        print("first_name - ", rollCall[x]['first_name'],"last_name - ", rollCall[x]['last_name'])
iterateDictionary(rollCall)

# get values from a  list of dictionaries

def iterateDictionary2(element):
    for a in range(0, len(element)):
        print(element[a]['first_name'])
    for b in range(0, len(element)):
        print(element[b]['last_name'])
iterateDictionary2(rollCall)

# iterate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(element):
    print(len (element['locations']), "LOCATIONS")
    for y in range(0, len(element['locations'])):
        print(element['locations'][y])
    print(len(element['instructors']), "INSTRUCTORS")
    for z in range(0, len(element['instructors'])):
        print(element['instructors'][z])
printInfo(dojo)