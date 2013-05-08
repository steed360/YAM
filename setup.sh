export DJANGO_SETTINGS_MODULE=yam.settings
python manage.py sqlclear yam | python manage.py dbshell 
python manage.py syncdb

python addData.py


