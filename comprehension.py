
# list comprehension

# [ <expression> for <arg> in <list> if <condition> ]

listofWords = ["hello", "python", "world", "experts", "fun"]

result = []

for word in listofWords:
    result.append(word[0])
    

print(result)

# list comprehension
result2 = [word[0:2] for word in listofWords if word != 'experts']

print(result2)

numbers = [4, 10, -5, 200]
# multiply each item by 3
# ignore negative numbers

matrix = [[1,2,6], [7, 8, 10], [100, 5, 2]]
# create a list of first item in each list







