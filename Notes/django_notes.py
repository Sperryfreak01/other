# Preps & Setup for Django development environment
"""
Setup:
1) Download & install Anaconda (comes with mega packages). Allow it to set PATH variables.

2) Use "conda list" to see what packages & verions came with Anaconda originally

3) Use "conda update" or "conda install" to update or install any packages needed (Pillow, pip, psycopg2, etc)

4) Use "conda create -n test_env package1 package2 package3 packageX" to create a virtual env with the 
designated packages installed up-to-date

5) Activate newly created env with "activate test_env"

6) cd into the new activated env 

7) Start a new django project "python .\Scripts\django-admin.py startproject yourprojectname" or
git clone a repo with the code "git clone url"

8) Open pgAdmin III and create a new database table. Input the table's name into the settings.py file
under DATABASES (don't forget to have psycopg2 installed in the env)

9) Run "python manage.py makemigrations" and "python manage.py migrate" to setup the database

10) Run "python manage.py createsuperuser"
"""

# Git commands
"""
1) git init (in the directory you want git to create repository)
2) git status
3) git add --all
4) git commit -m "message"
5) git remote -v
5a) git remote add "name (usually 'origin')" location
5b) git remote add origin https://github.com/peteza33/suggest
6) git push origin master
"""

"""
---OLD---
1) Download Anaconda (comes with a shit ton of extra packages like matplotlib!)

2) Install PIP (move to the directory where the get-pip file is and type: "python get-pip.py")

3) Setup Environment variables in Windows System Settings under Advanced Settings:
C:\Python34;C:\Python34\python.exe;C:\Python34\Scripts\; C:\Python34\Lib\site-packages\django\bin­;

3a)Use conda to create a environment and pre-install defined packages:
conda create -p ~/Desktop/test_env python pip matplotlib pillow django (etc)

3b)OR: Install virtualenv: pip install virtualenv

!!REALLY START HERE!!
4)Move to Desktop and create & activate a virtual environment
cd desktop
virtualenv test_env
cd test_env
.\Scripts\activate

6) Install Django (if not already in the env from conda):
pip install django      or pip install django==1.X.Y (replace x and y for version numbers)

7) Start django project:
python .\Scripts\django-admin.py startproject yourprojectname
OR: git clone a repository with the sourcec code

7a) for PostgreSQL:
open pgAdmin III and create a new database table. Use that table name to edit the Settings
file under DATABASES to setup PostgreSQL. Don't forget to install psycopy2 into the virtualenv

8)Sync database and run server:
cd yourprojectname
python manage.py migrate
python manage.py runserver

9)setup text editor
Open Sublime text
Project/save project as: then put the file in the django virtual environment
Project/add folder: put in the actual project file (usually "src")

To make Model (database) changes:
a. change models.py
b. python manage.py makemigrations
c. python manage.py migrate
"""