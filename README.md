
YAM (in progress)
----

- A Django based online nutrition advisor.
- Add ingredients of a meal and the app will calculate the
nutrition content. 
- Later releases will advise on ingredients to fill nutrition
gaps and produce shopping lists.


Getting started:

export DJANGO_SETTINGS_MODULE=yam.settings
python manage.py sqlclear yam | python manage.py dbshell 
python manage.py syncdb


