# Dictionary
# Hashmap -- key : value
# key may appear only once - single appearence
#12 -- moshe
#14 -- moshe
#12 -- danny
# 2 keys have the same value
#
#
#   3,4,5             moshe, danny, tamar
#
# key - may be anything

# [1,2,3]  #adress 4005
# [1,2,3]

# create dictionary for cities population
# TLV, LONDON, PARIS, TOKYO
# input city name -- print population

popMap = { 'TEL AVIV' : 443939, 'LONDON' : 8825000, 'PARIS' : 0,'TOKYO' : 13929286}

cityName = input("Please enter a city name: ")
print(f'{cityName} population is: {popMap[cityName.upper()]}')
