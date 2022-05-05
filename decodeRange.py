import re
def decodeRange():
    range = input("Enter range of episodes: ")

    if re.match("\ *",range) or range == "":
        return None
    inputs = range.split(" ")
    revisedInputs = []
    for x in inputs:
        if re.match("\d+\d+\-\d+\d*|(\d+\,)+\d*|(\d+)+",x) != None and not re.search("[a-zA-z]",x):
            revisedInputs.append(x)

    groupNumbers = []
    ranges = []
    individualNumbers = []

    for x in revisedInputs:
        if re.search("-",x) and not re.search("a-zA-Z",x):
            ranges.append(x)
        elif re.match("\d+\d*\-\d+\d*|(\d+\,)+\d*",x) and not re.search("a-zA-Z",x):
            groupNumbers.append(x)
        elif re.match("(\d+)+",x):
            individualNumbers.append(x)
    splittedRanges = []
    for x in ranges:
        splittedRanges.append(tuple(x.split("-")))

    numbersSet = set()

    for x in splittedRanges:
        if int(x[0]) > int(x[1]):
            splittedRanges.remove(x)

    for x in splittedRanges:
        index = int(x[0])
        while index <= int(x[1]):
            numbersSet.add(index)
            index = index +1

    splittedNumbersLists = []

    for x in groupNumbers:
        splittedNumbersLists.append(x.split(","))

    for x in splittedNumbersLists:
        for y in x:
            if y == "":
                x.remove(y)

    for x in splittedNumbersLists:
        for y in x:
            numbersSet.add(int(y))    


    for x in individualNumbers:
        numbersSet.add(int(x))

    numbersList = list(numbersSet)
    numbersList.sort()
    return numbersList