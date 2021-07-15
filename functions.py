# downloadManager 
from os.path import isdir 

def err():
    print('Wrong data')
    exit()

def validateNumber(number):
    try:
        number = int(number)
        return number
    except: err()

def validateDir(directory): 
    if isdir(directory) == False: err()
    else: return directory 

def enterData():
    numLinks = input('Enter the number of links: ')
    numLinks = validateNumber(numLinks)
    directory = input('Enter the download path: ')
    directory = validateDir(directory)
    return numLinks, directory

(numLinks, directory) = enterData()
