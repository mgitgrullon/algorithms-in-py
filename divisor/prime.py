def divisors(integer):
  if type(integer) is not int:
    raise TypeError("Value must be Integer")
  result = []
  for i in range(2, integer):
    if integer % i == 0:
      result.append(i)

  # return (str(integer) + " is prime") if len(result) == 0 else result
  return (result, (str(integer) + " is prime"))[len(result) == 0]