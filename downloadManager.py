from functions import enterData, storeData, printData

(numLinks, directory, fileName) = enterData()

data = storeData(numLinks)

printData(directory, fileName, data, numLinks)
