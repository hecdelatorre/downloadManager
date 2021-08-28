from os.path import isdir 
from getpass import getuser
from bullet import Input, YesNo, Numbers, colors
from colored import fg, attr

colorRed = fg('#CC0000')
colorGreen = fg('#73D216')
colorBlue = fg('#338CFF')
res = attr('reset')

def err():
    print(f'{colorRed}Wrong data{res}')
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
    numLinks = Numbers(f'{colorGreen}Enter the number of links: {res}', word_color = colors.foreground["yellow"], type=int).launch()
    directory = Input(f'{colorGreen}Enter the download path: {res}', default = f"/home/{getuser()}/Downloads", word_color = colors.foreground["yellow"]).launch()
    directory = validateDir(directory)
    fileName = Input(f'{colorGreen}Enter the executable name: {res}', default = "default", word_color = colors.foreground["yellow"]).launch()
    return numLinks, directory, fileName

def storeData(numLinks):
    data = []
    createDirectory = YesNo(f'{colorGreen}Create directory to store downloaded files? {res}', default = 'n', word_color = colors.foreground["yellow"]).launch()
    if createDirectory:
        newDirectory = Input(f'{colorGreen}Enter the name of the directory to create: {res}', default='default', word_color = colors.foreground["yellow"]).launch()
        newDirectory = f"mkdir '{newDirectory}' && cd '{newDirectory}'"
        data.append(newDirectory)

    for i in range(0, numLinks, 1):
        link = Input(f'{colorBlue}Enter the link {i+1} of {numLinks}: {res}', word_color = colors.foreground["yellow"]).launch()
        data.append(link)

    return data

def printData(directory, fileName, data, numLinks):
    print()
    file = open(f"{directory}/{fileName}.sh", "w")
    startTime = "date +'StartTime: %D %r'"
    print(startTime)
    file.write(f'{startTime}\n')
    count, c = 0, 1

    for dat in data:
        if count == 0 and data[count].find('mkdir') == 0:
            print(data[count])
            file.write(f'{data[count]}\n')
        else:
            linkFormat = f"echo -e '\\n  File {c} of {numLinks}'\naria2c -c --seed-time=0 '{dat}'"
            print(linkFormat)
            file.write(f'{linkFormat}\n')
            c += 1
        count += 1

    endTime = "date +'EndTime: %D %r'"
    print(endTime)
    file.write(endTime)
    file.close()
