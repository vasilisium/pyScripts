import os
from shutil import copy
# import codecs
# from shutil import copy
# import ntpath

files_name_pices = {
	# 'Z:\\zavyalov\\81\\files\\meizu\\sd': [
	# 	'14-412',
	# 	'14-411',
	# 	'14-356',
	# 	'14-438',
	# 	'14-440',
	# 	'14-441',
	# 	'14-443',
	# 	'14-450',
	# 	'14-451',
	# ],
	'Z:\\zavyalov\\81\\files\\samsung_phone\\phone': [
		'a1aeaaf9241d525b4961478e64ad5808',
		'dce005766c37b3507409f43a856f293d',
		'eb728511c839ea5a482c552a5b55f81e', # ????
		'EPORNER.COM -  wgSRHeCojsG  Chicks Get The Sex Party Going (1080).mp4',
		'EPORNER.COM 20- 20 0k4BNUa6I5v  20Mila 20Azul 20- 20Hihg 20Noon 20Heat 20(1.mp4',
		'EPORNER.COM 20- 20 jOvzwVNbrvp  20Teens 20Looking 20For 20A 20Perfect 20Sex.mp4',
		'EPORNER.COM 20- 20 x1P3EHRH9oD  20Milla 20Azul 20- 20Burn 20For 20You 20(10.mp4',
	],
	'Z:\\zavyalov\\81\\files\\samsung_phone\\sd': [
		'1-371',
		'1-372',
		'1-373',
		'1-374',
		'1-375',
		'1-376',
		'1-377',
		'1-379',
		'1-380',
		'1-381',
		'1-382',
		'1-383',
		'1-384',
		'1-385',
		'1-386',
		'1-387',
		'1-388',
		'1-389',
		'1-390',
		'1-391',
		'1-392',
		'1-393',
		'1-394',
		'1-395',
		'1-396',
		'1-397',
		'1-406',
		'1-406',
		'1-419',
		'1-421',
		'1-422',
		'1-484',
	],
	'Z:\\zavyalov\\81\\files\\samsung_table\\sd': [
		'1-1440',
		'1-1438', # ???
		'1-1437',
		'1-1436',
		'1-1435',
		'1-1434',
		'1-1433',
		'1-1432',
		'1-1431',
		'1-1430',
		'1-1427',
		'1-1424',
		'1-378',
		'1-377',
		'1-377',
		'1-376',
		'1-335',
		'1-334',
		'1-333',
		'1-332',
		'1-310',
		'1-309',
	],
	'Z:\\zavyalov\\81\\files\\samsung_table\\tablePC': [
		'ortofzoo-animal-girl-horse-sex-lara.mp4',
		'd9211a58d6f1acbe873dcba005be0e62',
		'b194e993f4aa5653f7cc57661f992bcd',
		'144364.mp4',
		'1077ca0eb21d018f4ef6eae7a558f5ab',
	]
}

# rootPath = 'Z:\\zavyalov\\81\\files'
destPath = 'Z:\\zavyalov\\81\\porn'

for folder in files_name_pices:
    for f in files_name_pices[folder]:
        dir_Files = os.listdir(folder)
        for f1 in dir_Files:
            if f in f1:
                folderToCopy = folder.split('\\')[-2:]
                folderToCopy = os.path.join(destPath, *folderToCopy)
                if not os.path.exists(folderToCopy):
                    os.makedirs(folderToCopy)
                file_name = os.path.join(folder, f1)
                copy(file_name, folderToCopy)