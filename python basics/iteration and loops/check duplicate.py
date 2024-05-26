def hasDuplicates(list):
  for i in list:
    count = 0
    for j in list:
        if i == j:
            count += 1
    if count > 1:
        return True
  return False