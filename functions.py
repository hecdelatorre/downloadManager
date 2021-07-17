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
    fileName = input('Enter the executable name: ')
    return numLinks, directory, fileName

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

def printData(directory, fileName, data, numLinks):
    file = open(f"{directory}/{fileName}.sh", "w")
    startTime = "echo -e '\\n' && date +'StartTime: %D %r' && echo -e '\\n'"
    print(startTime)
    file.write(f'{startTime}\n')
    count = 0

    for dat in data:
        if count == 0 and data[count].find('mkdir') == 0:
            print(data[count])
            file.write(f'{data[count]}\n')
        else:
            linkFormat = f"echo -e ' File {count + 1} of {numLinks}\\n'\nwget --retry-connrefused -nc '{dat}'"
            print(linkFormat)
            file.write(f'{linkFormat}\n')
        count += 1

    endTime = "date +'EndTime: %D %r'"
    print(endTime)
    file.write(endTime)
    file.close()
