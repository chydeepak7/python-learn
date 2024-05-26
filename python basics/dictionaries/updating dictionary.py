def updateAges(ages, n):
  for i,j in ages.items():
    ages[i] += n
  return ages

test = {
    'deepak': 10,
'manjit': 34,
'anish': 31
}
print(updateAges(test,6))