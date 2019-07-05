
# dictionary :
# create dictionary i.e. { 1 : 'moshe', 2: 'erez', 3: 'dana' }
# create function - parameters gets dictionary, key
#  retrun True if key exist and False if not exist

def doesKeyExist(d, k):
    '''
    checks if key exists in dictionary
    :param d: dictionary
    :param k: key
    :return: True if k exist in d
    '''
    # return k in d.keys() -- shorter
    if k in d.keys():
        return True
    else:
        return False

def tryAddValue(d, k, v):
    '''
    add [k,v] to dictionary if k does not exist
    :param d: dictionary
    :param k: key
    :param v: value
    :return: True if [k,v] was added , False if not
    '''
    pass

myDict = { 1 : 'moshe', 2: 'erez', 3: 'dana' }


# print value of key: myDict[1]
# add/replace value of key: myDict[5] = 'sharon'
# add/replace value of key: myDict[79] = 'danny'
# list(myDict.values())
# list(myDict.keys())


if doesKeyExist(myDict, 5) == False:
    myDict[5] = 'anat'

if doesKeyExist(myDict, 4) == False:
    myDict[4] = 'rona'

print(myDict)
