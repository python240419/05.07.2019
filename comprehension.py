
# list comprehension

# [ <expression> for <arg> in <list> if <condition> ]

listofWords = ["hello", "python", "world", "experts", "fun"]

result = []

for word in listofWords:
    result.append(word[0])

print(word) # word still exists

print(result)

# list comprehension
result2 = [word[0:2] for word in listofWords if word != 'experts']

print(result2)

numbers = [4, 10, -5, 200]
# multiply each item by 3
# ignore negative numbers

numbers3 = [x*3 for x in numbers if x > 0]
print(numbers3)

# print(x) -- error

matrix = [[1,2,6], [7, 8, 10], [100, 5, 2]]
# create a list of first item in each list

# one row
rows = [oneList[0] for oneList in matrix]

# all rows
# matrix = [[1,2,6], [7], [100, 5, 2]]
for i in range(len(matrix)):
    rows = [oneList[i] for oneList in matrix if i < len(oneList)]
    print(rows)

l1 = list(range(10))
print(l1)

numbers = [2, 6, 10, 200, -20, 3]
l2 = [x for x in range(0, 10, 2) if x % 2 == 0]
print(l2)

# create list of numbers sqr 1, 2, 4, 9, 16, 25, 36 ... 1-20
# create list of numbers between 1-100 which can divide by 3 or 5 or 7 without reminder
# [5.9, 0.9, -9.2, 10.1] => [5, 0, -9, 10]










