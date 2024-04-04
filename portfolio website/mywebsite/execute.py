import os
a = os.getcwd()
os.system("cd '{a}'")
os.system("start manage.py runserver")
os.system("start http://127.0.0.1:8000/")
