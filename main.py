i = int(input("Input a number: "))

lst = []
for n in range(1, i+1):
  if n % 3 == 0 and n % 5 == 0:
    lst.append("FizzBuzz")
  elif n % 3 == 0:
    lst.append("Fizz")
  elif n % 5 == 0:
    lst.append("Buzz")
  else:
    lst.append(str(n))

print(lst)
