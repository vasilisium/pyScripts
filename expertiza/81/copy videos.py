import os
import codecs
from shutil import copy
import ntpath

rootPath = 'Z:/zavyalov/81/sams_tablepc/mefe/samsung SM-T561 (2018-11-21 10h24m52s)/html_files'
destPath = './tablePC/'

files = os.listdir()

for file in files:
    if file.endswith('.txt'):
        copyTo = file[0:-4]
        reader = codecs.open(file, "r", "utf_8_sig" )
        errCount = 1
        linenumber = 1
        for line in reader:
            filePath = os.path.abspath(os.path.join(rootPath, line[:-2]))
            # copyToPath = os.path.join(os.path.abspath(destPath), ntpath.basename(line[:-2]))
            copyToPath = os.path.abspath(destPath)
            # print(filePath, os.path.abspath(destPath))
            try:
                copy(filePath, copyToPath)
            except Exception as ex:
                print(str(linenumber) + ':' + line[:-2])
                errCount += 1
            linenumber += 1
            
        reader.close()
