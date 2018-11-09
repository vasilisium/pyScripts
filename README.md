# pyScripts
pyScripts
# update all pip puckages
pip list -o --format json | ConvertFrom-Json | foreach {pip install $_.name -U --no-warn-script-location}
pip uninstall -r requirements.txt
