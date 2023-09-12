rm db.sqlite3
rm -rf ./furxapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations furxapi
python3 manage.py migrate furxapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata furxprofile
python3 manage.py loaddata registryitem
python3 manage.py loaddata todolist
python3 manage.py loaddata feeling
python3 manage.py loaddata blog
