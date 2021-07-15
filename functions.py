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

# (numLinks, directory) = enterData()

def storeData(numLinks):
    data = []
    createDirectory = input('Create directory to store downloaded files? y (Enter skip) ')
    if createDirectory == 'y':
        newDirectory = input('Enter the name of the directory to create: ')
        newDirectory = f"mkdir '{newDirectory}' && cd '{newDirectory}'"
        data.append(newDirectory)

    for i in range(0, numLinks, 1):
        link = input(f'Enter the link {i+1} of {numLinks}: ')
        data.append(link)

    return data
