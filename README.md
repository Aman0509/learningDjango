# Learn Django (for beginners)

## Introduction

Django is a Python-based web framework which allows you to quickly create web application without all of the installation or dependency problems that you normally will find with other frameworks. For more info, [click here](https://www.geeksforgeeks.org/django-basics/)

**Other useful readings**

- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [W3Schools](https://www.w3schools.com/django/index.php)
- [My Notes](https://github.com/Aman0509/learningDjango/blob/main/other/Django.pdf)

### 1. Installing Django

You may create first virtual environment or install it globally. Use below command to install Django:

```
pip install Django
```

### 2. Creating a Django Project

Once Django is installed, you have to create a Django project. For that, use below command:

```
django-admin startproject <project_name>
```

*For example*

```
django-admin startproject myproject
```

It will create your **_myproject_** project which has below file structure

```
myproject
├── manage.py
└── myproject
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### 3. Analyzing the created project

Please refer below links to understand the Django project structure

- [Techvidvan - Django Project Structure and File Structure](https://techvidvan.com/tutorials/django-project-structure-layout/)
- [AskPython - Python Django App Structure and Project Structure](https://www.askpython.com/django/django-app-structure-project-structure)

### 4. Starting the Development Server

Django comes with built-in web server that is used for development purposes.\
To start it, use below command:

```
python manage.py runserver
```

### 5. Django Apps

Django projects embrace a modular structure. A Django project often consists of multiple modules that make up the project. Now in Django world, those modules are not called modules rather they are termed as app and you then do store your actual application code in those apps.\
To create an app, ensure you are inside your project and then run below command:

```
python3 manage.py startapp <app_name>
```

*For Example*

```
python3 manage.py startapp myapp1
```

It will create **_myapp1_** inside your project and now you will have below file structure.\
You can find information about each Django app component in the links shared for understanding Django project above.

```
myproject
├── db.sqlite3
├── manage.py
├── myapp1
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── myproject
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── settings.cpython-39.pyc
    │   ├── urls.cpython-39.pyc
    │   └── wsgi.cpython-39.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## URLs and Views

### 1. URL
![url academind slide image](https://github.com/Aman0509/learningDjango/blob/main/other/images/urls.png)

Readings:
- [Techvidvan - Django URLs and URL Mapping](https://techvidvan.com/tutorials/django-urls/)
- [Offical Django Docs - URL Dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

### 2. Views
![views academind slide image](https://github.com/Aman0509/learningDjango/blob/main/other/images/views-1.png)

![views academind slide image](https://github.com/Aman0509/learningDjango/blob/main/other/images/views-2.png)

![request and response academind slide image](https://github.com/Aman0509/learningDjango/blob/main/other/images/request_and_response.png)

Readings:
- [The Django Book - Mastering Django: Views](https://djangobook.com/django-tutorials/mastering-django-views/)

### [3. Monthly Challenges Project](https://github.com/Aman0509/learningDjango/blob/main/01-URLs_and_Views/MyChallenges)

In this project, below concepts were covered:
- Creating Views and URLs
- Dynamic Path Segments and Captured Values
- Path (Datatype) Converters
- Redirects
- Reverse Function and Named URLs


## FAQs

**Q - Is Django a web server and a framework?**\
A - Yes and no. Django has a built-in web server that's used for development purposes. This web server is used when you run the web app locally, such as when debugging in Visual Studio. When you deploy to a web host, however, Django uses the host's web server instead. The wsgi.py module in the Django project takes care of hooking into the production servers.


## References
- [Python Django - The Practical Guide By Academind](https://www.udemy.com/course/python-django-the-practical-guide/)
