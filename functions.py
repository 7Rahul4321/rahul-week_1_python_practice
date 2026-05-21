# program 1: print table of 8
def table(num):
  for i in range (1,11):
    print(num, "x", i, "=", num*i)
    table(5)

# program 2: square of a number
def square(num):
  result = num*num
  print("square is:" , result)

square(6)
