try:
  print(x)
except SyntaxError:
  print("Variable x is not defined")
except NameError:
  print("Something else went wrong")