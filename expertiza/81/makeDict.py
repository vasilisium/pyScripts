import codecs

fileName = 'chars.txt'
reader = codecs.open(fileName, "r", "utf_8_sig" )
l2 = reader.readline()[0:-2].split()
l1 = reader.readline()[0:-2].split()
# print(l1)
# print(l2)
file = open("dict.txt",'w')
i=0
for a in l1:
    try:
        print('l1: ' + a)
    except Exception as e:
        print('l1 переполнен')

    try:
        print(', l2: ' + l2[i]+'\r\n')
    except Exception as e:
        print(', l1 переполнен\r\n')
    
    file.write('\"' + a +'\" : \"' + l2[i] + '\",\r\n')
    i+=1
file.close()