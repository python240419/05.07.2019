
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
    #
    #
    #d.keys()
    #return True;

myDict = { 1 : 'moshe', 2: 'erez', 3: 'dana' }


# print value of key: myDict[1]
# add/replace value of key: myDict[5] = 'sharon'
# add/replace value of key: myDict[79] = 'danny'
# list(myDict.values())
# list(myDict.keys())


if doesKeyExist(myDict, 3) == False:
    myDict[3] = 'anat'

if doesKeyExist(myDict, 4) == False:
    myDict[4] = 'rona'
