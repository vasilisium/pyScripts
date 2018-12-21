import os
import codecs
import hashlib
from shutil import copy

# rootPath = 'Z:\\zavyalov\\81\\sams_phone\\mefe\\samsung SM-J730FM (2018-11-21 09h47m44s)\\html_files\\phone'
rootPath = 'Z:\\zavyalov\\81\\sams_tablepc\\mefe\\samsung SM-T561 (2018-11-21 10h24m52s)\\html_files\\phone'
# destPath = '.\\phone\\'
destPath = '.\\tablePC\\'

copyToPath = os.path.abspath(destPath)

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

files = os.listdir()
for txt in files:
    if txt.endswith('.txt'):
        hashes = []
        reader = codecs.open(txt, "r", "utf_8_sig" )
        for line in reader:
            hashes.append(line[0:-2])
        
        for root, subFolders, files in os.walk(rootPath):
            for f in files:
                file_path = os.path.join(root, f)
                h = sha256_checksum(file_path)
                if h.upper() in hashes:
                    print(file_path)
                    copy(file_path, copyToPath)