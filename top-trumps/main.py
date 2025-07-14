def main():
    print(convertToBinary(40, 8))
    return

from math import log2

def convertToBinary(num : int, amountOfDigits : int = -129) -> str:
    if amountOfDigits == -129:
        amountOfDigits = int(log2(num))
        
    if amountOfDigits == -1:
        return ""
    else:
        if num >= 2 ** amountOfDigits:
            return "1" + convertToBinary(num - 2 ** amountOfDigits ,amountOfDigits-1)
        else:
            return "0" + convertToBinary(num, amountOfDigits-1)

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

import json

def recursiveDictionaryPrint(dictionary : dict) -> None:
    for key in dictionary:
        print(f"{key}: " + "{")
        if type(dictionary[key]) == dict:
            recursiveDictionaryPrint(dictionary[key])
        if type(dictionary[key]) == list:
            listStr = f"{key} = ["
            for i in range(len(dictionary[key])):
                listStr += str(dictionary[key][i])
                if i + 1 != len(dictionary[key]):
                    listStr += ", "
            listStr += "]"
            print(listStr)
        else:
            print(f"{key} : {str(dictionary[key])}")
        print("}")
    pass



if __name__=="__main__":
    with open("sampleIdentifiers.json", "r") as dictionarySource:
        dictionary = json.load(dictionarySource)
    recursiveDictionaryPrint(dictionary)
    main()