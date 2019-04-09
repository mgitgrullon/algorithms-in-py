def array_diff(a, b):
  if type(a) is not list or type(b) is not list:
    raise TypeError("The params muy be a valid list")
  return [_ for _ in a if _ not in b]
