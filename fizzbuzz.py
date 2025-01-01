def solve(n):
  list = []
  for i in range(1, n + 1):
    if ((i % 3 == 0) and (i % 5 == 0)):
      list.append('FizzBuzz')
    elif i % 5 == 0:
      list.append('Buzz')
    elif i % 3 == 0:
      list.append('Fizz')
    else:
      list.append(i)

  return list

print("INPUT: 15")
print("OUTPUT: " + str(solve(15)))