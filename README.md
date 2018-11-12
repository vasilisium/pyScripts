# pyScripts
some of my snippets:)
# update all pip puckages
pip list -o --format json | ConvertFrom-Json | foreach {pip install $_.name -U --no-warn-script-location}

# del pip puckages
pip uninstall -r requirements.txt

#check executable path
python -c "import sys; print(sys.executable)"
