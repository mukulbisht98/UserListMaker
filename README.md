# USER ListMaker
this project creates a webpage including a database and a webserver which allows you to create new users in the database.

## Getting Started
You should have Basic understanding in Python, HTML, CSS & JS.
### Prerequisites
things you need to install :
1.) python
2.) sqlalchemy
### installing
1.) python or python3
```
sudo apt-get install python
```
or

```
sudo apt-get install python3
```
2.) sqlalchemy
```
 pip install SQLAlchemy==1.2.8
 ```

### Starting

#### tough way
first run database_setup.py to setup the database in your device.
```
python database_setup.py
```
to add users with python run newEntry.py
```
python newEntry.py
```
after database_setup and adding few users, run web_server.py
```
python web_server.py
```

#### easy way
Just run Webserver.py
```
python web_server.py
```
and ENJOY!!!

### On Browser
open [localhost:8080/users](localhost:8080/users) to view the usersList

you can add users by [localhost:8080/users/new](localhost:8080/users/new)
