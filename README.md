# pyScripts
some of my snippets:)

# update all pip puckages
pip list -o --format json | ConvertFrom-Json | foreach {pip install $_.name -U --no-warn-script-location}

# del pip puckages
pip uninstall -r requirements.txt

# venv issuse
run      python -m venv env --without-pip

activate env\Scripts\activate

run      C:\test\virtual\Scripts>python get-pip.py

# check executable path
python -c "import sys; print(sys.executable)"

# coins.py
coin parser from https://coinmarketcap.com/all/views/all/

# dbfImport.py
convert .dbf file to .xlsx 

to compile dbfImport.py to exe run: pyinstaller --onefile dbfImport.py
