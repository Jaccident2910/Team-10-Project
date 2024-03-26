# Documentation for Backend

## 1. Setting Up

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

#### Setup Files

After installing all the necessary dependencies, I created the following files:

* createDatabase.py , a program that creates a database named `accounts`, and then creates a table called `users` where user information will be stored.
* resetDatabase.py , a program that deletes the `accounts` database

