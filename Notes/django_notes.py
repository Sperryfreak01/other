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

to branch:
1) git branch name
2) git checkout name
3) git push origin name & git pull origin name
4) git checkout master
5) git merge name
6) git branch -D name
7) git push origin --delete name
"""