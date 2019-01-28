import collections

sen1 = "Hello what are you doing?"
sen2 = "Hello what you doing?"


def missingword(sen1, sen2):

  if sen1 == "" or sen1 == "":
    return False
    
  sen1 = sen1.replace('\r', '' ).split()
  sen2 = sen2.replace('\r', '' ).split()
  dictn = collections.defaultdict(int)

  for word in sen1:
    if word in dictn:
      dictn[word] += 1
    else:
      dictn[word] = 1

  for word in sen2:
    if word in dictn:
      dictn[word] -= 1
    else:
      dictn[word] += 1

  for word in dictn:
    if dictn[word] !=  0:
      return word

  return ""

print(missingword(sen1, sen2))