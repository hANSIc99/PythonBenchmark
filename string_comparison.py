import time


HashDict = dict[str, int]

def bechnStringCompareSimple():
    print('Hello World')


    testArray = [   'Test0', 'Test1', 'Test2', 'Test3', 'Test4',
                    'Test5', 'Test6', 'Test7', 'Test8', 'Test9']

    target_result = int((9 + 9**2) / 2) # gaussche summenformel
    actual_result = 0
    startTime = time.process_time()
    for testString in testArray:
        actual_result += checkString(testString)

    print('bechnStringCompareSimple() - Execution time: {}'.format(time.process_time() - startTime))

def checkString(testString):

    if testString == 'Test0':
        return 0
    elif testString == 'Test1':
        return 1
    elif testString == 'Test2':
        return 2
    elif testString == 'Test3':
        return 3
    elif testString == 'Test4':
        return 4
    elif testString == 'Test5':
        return 5
    elif testString == 'Test6':
        return 6
    elif testString == 'Test7':
        return 7
    elif testString == 'Test8':
        return 8
    elif testString == 'Test9':
        return 9


def benchStrinCompareHash():

    testArray = [   'Test0', 'Test1', 'Test2', 'Test3', 'Test4',
                    'Test5', 'Test6', 'Test7', 'Test8', 'Test9']

    def hashStr(inStr : str) -> int:
        return hash(inStr)

    #hashList = list(map(hashStr, testArray))

    hashDict = { key : hash(key) for key in testArray}
    actual_result = 0
    startTime = time.process_time()
    for testString in testArray:
        actual_result += checkStringHash(hashDict, testString)
    print('bechnStringCompareHash() - Execution time: {}'.format(time.process_time() - startTime))



def checkStringHash(hashDict : HashDict, testString : str) -> int:

    if hashDict.get('Test0') == hash(testString):
        return 0
    elif hashDict.get('Test1') == hash(testString):
        return 1
    elif hashDict.get('Test2') == hash(testString):
        return 2
    elif hashDict.get('Test3') == hash(testString):
        return 3
    elif hashDict.get('Test4') == hash(testString):
        return 4
    elif hashDict.get('Test5') == hash(testString):
        return 5
    elif hashDict.get('Test6') == hash(testString):
        return 6
    elif hashDict.get('Test7') == hash(testString):
        return 7
    elif hashDict.get('Test8') == hash(testString):
        return 8
    elif hashDict.get('Test9') == hash(testString):
        return 9

def benchStrinCompareHash2():

    testArray = [   'Test0', 'Test1', 'Test2', 'Test3', 'Test4',
                    'Test5', 'Test6', 'Test7', 'Test8', 'Test9']

    def hashStr(inStr : str) -> int:
        return hash(inStr)

    hashList = list(map(hashStr, testArray))

    hashDict = { key : hash(key) for key in testArray}
    actual_result = 0
    startTime = time.process_time()
    for testHash in hashList:
        actual_result += checkStringHash2(hashDict, testHash)
    print('bechnStringCompareHash2() - Execution time: {}'.format(time.process_time() - startTime))

def checkStringHash2(hashDict : HashDict, testStringHash : int) -> int:

    if hashDict.get('Test0') == testStringHash:
        return 0
    elif hashDict.get('Test1') == testStringHash:
        return 1
    elif hashDict.get('Test2') == testStringHash:
        return 2
    elif hashDict.get('Test3') == testStringHash:
        return 3
    elif hashDict.get('Test4') == testStringHash:
        return 4
    elif hashDict.get('Test5') == testStringHash:
        return 5
    elif hashDict.get('Test6') == testStringHash:
        return 6
    elif hashDict.get('Test7') == testStringHash:
        return 7
    elif hashDict.get('Test8') == testStringHash:
        return 8
    elif hashDict.get('Test9') == testStringHash:
        return 9


def benchStrinCompareDispatch():

    testArray = [   'Test0', 'Test1', 'Test2', 'Test3', 'Test4',
                    'Test5', 'Test6', 'Test7', 'Test8', 'Test9']


    dispatch = {
        'Test0' : lambda : 0,
        'Test1' : lambda : 1,
        'Test2' : lambda : 2,
        'Test3' : lambda : 3,
        'Test4' : lambda : 4,
        'Test5' : lambda : 5,
        'Test6' : lambda : 6,
        'Test7' : lambda : 7,
        'Test8' : lambda : 8,
        'Test9' : lambda : 9
    }
    actual_result = 0

    startTime = time.process_time()
    for testString in testArray:
        try:
            actual_result += dispatch[testString]()
        except KeyError as e:
            continue
        
    print('benchStrinCompareDispatch() - Execution time: {}'.format(time.process_time() - startTime))