# Documentation for Backend

## 1. Setting Up

### Installation Process for Windows

#### Installing MySQL

This can be downloaded from the mysql website [here](https://dev.mysql.com/downloads/installer/).

This project has been build with MySQL version 0.8.29-1.

You should set the root password to T3am10ftw!

### Installing Python Dependencies

You now need to install a number of libraries that this project depends on. These are Django, `mysqlclient` and `mysql-connector-python`.

You can install these dependencies by running the following commands in the command line:

```
py -m pip install django;
py -m pip install mysqlclient;
py -m pip install mysql-connector-python
```

We use Django version 5.0.3 in this project.

### Setup Files
The following python programs have been created to make setting up the database easier:

* createDatabase.py , a program that creates a database named `accounts`, and then creates a table called `users` where user information will be stored.
* resetDatabase.py , a program that deletes the `accounts` database

You should also go to the `application` folder in this project, and run the following commands:

```
py manage.py makemigrations
py manage.py migrate auth
my manage.py migrate
```

### Running the Server

You can begin running the server by running the following command in the `application` folder: 
```
py manage.py runserver
```

You can then find the website [here](http://127.0.0.1:8000/).



### Installation Process for Linux (Ubuntu)

In this part of the document I am going to document the process by which I got MySQL set up on my local computer, and then afterwards I will explain how to set up the rest of the backend - it is my hope that I will be able to create a bash file or makefile that will do most of this part for us.

#### Installing MySQL

The first step is to add the MySQL APT repository to your machine using the instructions found [here](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-setup)

I have used MySQL version 0.8.29-1 on my machine.

I made the root password T3am10ftw!

#### Installing Python Dependencies
I now want to install the relevant packages to create this backend on python, these being mysql.connector and django.

```
pip install django;
pip install mysqlclient;
pip install mysql-connector-python
```

This project uses Django version 5.0.3

when trying to install `mysqlclient` I ran into some issues with dependencies. Running
```
sudo apt-get install python3-dev default-libmysqlclient-dev build essential pkg-config
```
Solved the issue.

I then ran
```
python3 manage.py migrate
```
in the application folder.

#### Setup Files

After installing all the necessary dependencies, I created the following files:

* createDatabase.py , a program that creates a database named `accounts`, and then creates a table called `users` where user information will be stored.
* resetDatabase.py , a program that deletes the `accounts` database



