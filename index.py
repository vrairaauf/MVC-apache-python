#! C:\Users\mohamed\AppData\Local\Programs\Python\Python38\python.exe
import cgi
form=cgi.FieldStorage()
from controller import *
print("Content-type: text/html\n\n")
print(form['method'])
posts()
