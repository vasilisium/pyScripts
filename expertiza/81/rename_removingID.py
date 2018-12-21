import os
import re

regex=re.compile(r'\d+-\d+\s')

rootPath = 'Z:\\zavyalov\\81\\porn'

def removeID(filename):
    newFileName = filename
    newFileName = regex.sub('', newFileName)
    return newFileName

for root, subFolders, files in os.walk(rootPath):
    for file in files:
        if regex.match(file):
            new_file_name = regex.sub('', file)

            full_File_Path = os.path.join(root, file)
            new_full_File_Path = os.path.join(root, new_file_name)

            print(f'renaming the:\"{full_File_Path}\" to \"{new_full_File_Path}\"\r\n')
            os.rename(full_File_Path, new_full_File_Path)