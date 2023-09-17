# Python Loops & Conditionals

## Conditionals
n = 2

if n == 1:
	print(f"{n} is equal to 1")
elif n > 2:
	print(f"{n} is greater than 2")
else:
	print(n)

## Loops
for i in range(10):
	print(i)

while n < 10:
	print(n)
	n += 1

## List Comprehension
list1 = [i for i in range(10)]
list2 = [i for i in range(10) if i%2 == 0]