=========Read Me==============

Setup Database for application
1. Install postgresql:
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
2. Create database and user password:
    sudo -i -u postgres
    psql
    create database dbName;
    alter user postgres password ‘password’;
3. Run Database migration commands
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade