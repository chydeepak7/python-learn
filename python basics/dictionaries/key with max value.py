ages = {
     "Peter": 10,
     "Isabel": 191,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 130,
 }

key = list(ages.keys())
val = list(ages.values())
print(key[val.index(max(val))])
