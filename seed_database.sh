rm db.sqlite3
rm -rf ./furxapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations furxapi
python3 manage.py migrate furxapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata customers
python3 manage.py loaddata employees
python3 manage.py loaddata tickets