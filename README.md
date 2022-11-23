# buddy_advice_api

This project is a simple Django API of a project where the user can create products and comment on existing ones. 

## Setup

&nbsp; In order to run this project on your machine, it's need to follow these steps.

1º clone this repository:  

``` git clone https://github.com/eduardoyanoliveira/buddy_advice_api.git ```

2º Create a python virtual envirioment on the folder

```
  py -m venv venv
```

3º Activate the virtual env:

```
  venv\scripts\activate
```

4º Install the dependecies of the project if the following command

```
  pip install -r requirements.txt
```

5º Generate all the migration scripts for the database

```
  py manage.py makemigrations
```

5º Execute the migration scripts on database (It is possible to configure a specific database on the core\settings.py . If none is configured, an sqlite database will be auto generated).

```
  py manage.py migrate
```

6º Execute localy the API

```
  py manage.py runserver
```

7º In order to run the web application keep following the tutorial on the nebula-web-application repository

## Main Technologies

  - Python
  - Django
  - Django Rest Framework
  - Simple-JWT
  - Pillow
  - SQLite

  
