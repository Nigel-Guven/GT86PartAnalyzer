import os

def getCurrentPath():
    path = os.getcwd()
    print(path)

def switchToRawPath(new_path):
    os.chdir(new_path)
    getCurrentPath()

def switchToProcessedPath(new_path):
    os.chdir("..\\..\\..\\..")
    os.chdir(new_path)
    getCurrentPath()

def createDirectoryIfNotExists(new_path):
    if not os.path.exists(new_path):
            os.makedirs(new_path)

def formatPrice(price):
    price = price.strip().replace(',','')
    return "{:.{}f}".format(float(price), 2)

def isBlank(text):
    return not (text and text.strip())


