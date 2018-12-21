import os
import re
from dict import decDict

rootPath = 'D:\\Дослідження\\Експертизи\\2018\\81\\prog\\phone'

decoder = {}
keys = decDict.keys()
for key in keys:
    regex = re.compile(key)
    decoder[regex] = decDict[key]


def decode(filename):
    newFileName = filename
    for regex in decoder:
        newFileName = regex.sub(decoder[regex], newFileName)
    return newFileName

for root, subFolders, files in os.walk(rootPath):
    for file in files:
        if any(simbol in file for simbol in keys):
            newFileName = decode(file)
            fullFilePath = os.path.join(root, file)
            newfullFilePath = os.path.join(root, newFileName)
            print(f'renaming the:\"{fullFilePath}\" to \"{newfullFilePath}\"\r\n')
            os.rename(fullFilePath, newfullFilePath)