# Dictionary Assignment
# print(dir(myFriends)) to get the built-in methods and attributes of myFriends

myFriends = {
  'first' : ['Peter', 38, 'Red'],
  'second' : ['John', 34, 'Blue'],
  'third' : ['Mavis', 35, 'Green'],
  'fourth' : ['George', 29, 'Black'],
  'fifth' : ['Jonathan', 70, 'Silver']
  }

print(myFriends)


friendsList = [
myFriends['first'][0],
myFriends['second'][0],
myFriends['third'][0],
myFriends['fourth'][0],
myFriends['fifth'][0]
]

print(friendsList)


myFriends.update({'first' : ['Peter', 36, 'Red']})
print(myFriends)

myFriends.pop('third')
print(myFriends)


