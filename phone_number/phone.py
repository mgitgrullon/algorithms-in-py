def create_phone_number(n):
  string = ''
  for val in n:
    string += str(val) # '1234'
  result = "(" + string[:3] + ") " + string[3:6] + "-" + string[6:10]
  return result
