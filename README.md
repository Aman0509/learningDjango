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

## Templates and Static Files

### 1. Adding, Registering & Rendering Templates

- After creating the apps, ensure to register or update your app name in the INSTALLED_APP list in settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'challenges',  # --> app name 'challenges' added
]
```
- By doing this, Django will look for all the app level templates in the directory 'templates/<app_name>'. These directories needs to be created for each apps.

```
challenges  # --> app created
├── migrations
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-39.pyc
├── models.py
├── templates  # --> templates directory created
│   └── challenges
│       └── challenge_page.html
├── tests.py
├── urls.py
└── views.py
```

- Why are we creating <app_name>(challenges) directory inside 'templates' directory at app level?\
Let's say if you have a template exist in multiple apps with a same name then Django will not be able to tell them apart and merge all of them.
- If you have other templates outside your app, maybe some global templates used by multiple apps, then the path of these templates exists in some directory needs to be added in DIRS list in settings.py

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   # --> If you are creating a template folder at global level of your project then you have to mention the path of your template folder here.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Please check the implementation about the template renders here, [views.py](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/views.py) to know about rendering of templates.

### 2. Django Template Language

![DTL academind slide image](https://github.com/Aman0509/learningDjango/blob/main/other/images/dtl.png)

### 3. Filters

Readings:
- [GeeksforGeeks - Django Template Filters](https://www.geeksforgeeks.org/django-template-filters/#:~:text=Django%20Template%20Engine%20provides%20filters,it%20to%20one's%20own%20need.)
- [Official Docs - Built-in template tags and filters](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

Why Filter?\
You want to limit the work you do in the view and really restrict it to your core business logic which might be needed for fetching and transforming the data and when it comes to formatting and outputting the data you might wanna do as much of that logic in the template and filters are a great tool for that.

### 4. Tags

Readings:
- [GeeksforGeeks - Django Template Tags](https://www.geeksforgeeks.org/django-template-tags/)

[for](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#for) and [url](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#url) tags usage can be seen here, [index.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) and for [if](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#if), refer [challenge_page.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html)

### 5. Template Inheritance

- As a best practice, parent templates are created at project root level since other apps will inherit these and creating at app level doesn't make much sense.

- Create 'templates' directory at project root level and update its path in **settings.py** like below:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")], # <--
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Readings:
- [GeeksforGeeks - extends: Django Template Tags](https://www.geeksforgeeks.org/extends-django-template-tags/)

Check out the [parent template(base.html)](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/templates/base.html) and how [index.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) & [challenge_page.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html) are extending parent template.

### 6. Including Partial Template Snippets

When we have HTML snippets which needs to be used by some templates but not all the templates, in that case, we can make use of **_include_** tag.

An example could be navigation bar. In a big website, there might be few pages which may used same navigation bar.

This can be implement at app level. In our example, we will create a nav bar which will redirect us to the 'challenges' route. Implementation can be see here, [header.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/includes/header.html) and [challenge_page.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html). A directory 'includes'(you can give any other name as well) is created inside 'templates' dir in challenges app and inside that _header.html_ is created.  

**Notes**
- The included snippets here will have access to the same variables you have access to in the template where you include them. For example, in challenge_page.html, we have variable 'month' that would also be available in that included template. But for index.html, this variable cannot be accessed.

- You can also pass in specific context, specific values for the included template. You do this with the **_with_** keyword and then you can set extra variables which will be available inside of the included snippet which are not available in the template which is including.

For example, let say, in challenge.html, if you do like below:

```
{% block content %}
{% include "challenges/includes/header.html" with active_page="challenge" %}
.
.
.
```
and let's say, your header.html is updated like below:

```
<header>
  <nav>
    <a href="{% url "index" %}">All Challenges</a>
  </nav>
</header>
{{ active_page }}
```
then along with this navbar, it will also render the value of 'active_page' variable.

### 7. More on Django Template Language (DTL)

<u>**Accessing Dictionary Fields in Templates**</u>

When accessing dictionary data in a template, you DON'T use this syntax:

```
{{ myDictionary['some_key'] }}
```

Instead, you use the dot notation - as if it were a regular Python object:

```
{{ myDictionary.some_key }}
```

This might look strange, but keep in mind, that the DTL is a custom-made language. It looks like Python, but ultimately it is NOT Python - it's a language parsed and executed by Django. Hence, its syntax can deviate - just as it does here.

<u>**Calling Functions in Templates**</u>

Calling functions in templates also works differently than it does in Python.
Instead of calling it, you use functions like regular variables or properties.
i.e., instead of:

```
{{ result_from_a_function() }}
```

you would use

```
{{ result_from_a_function }}
```

### 8. 404 Template

Check out the implementation at [views.py](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/views.py)

In our example project, if user hit URL which does not exist, we will get below 404 and not the template created for it. In order to render our 404 template, we need to set ***DEBUG=False*** in _settings.py_, however, with that, Django development web server will not start. Our 404 page can be render when we deploy our application.

![404 academind screenshot](https://github.com/Aman0509/learningDjango/blob/main/other/images/404.png)


### 9. Adding Static Files

Readings:
- [Official Docs - How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/4.0/howto/static-files/)
- [LearnDjango - Djang)o Static Files and Templates](https://learndjango.com/tutorials/django-static-files)
- [Digital Ocean - Working with Django Templates & Static Files](https://www.digitalocean.com/community/tutorials/working-with-django-templates-static-files)

Checkout implementation of static files at app level here, [index.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) (css file, [challenges.css](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/challenges/static/challenges/challenges.css) is added at app level at path <app_name>/static/<app_name>/<css_file>)

Static file implementation at global level can be find here, [base.html](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/templates/base.html). To let Django know about global level static files ensure defining a list of directories (**STATICFILES_DIRS**) in your settings ([settings.py](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/MyChallenges/settings.py)) file where Django will also look for static files.

<u>**Building Static URLs Dynamically**</u>

Imagine, that you want to build a static URL where some part of the URL (e.g. the filename) is actually stored in a variable that's exposed to the template.
So you might want to build the URL like this:

```
{% static "my_path/to/" + the_file %}
```
Here, "the_file" would be a variable holding the actual filename.\
The above code would fail.

Instead, you can use the "add" filter provided by Django to construct this path dynamically:

```
{% static "my_path/to/"|add:the_file %}
```

### [10. Monthly Challenges Project](https://github.com/Aman0509/learningDjango/blob/main/02-Templates_and_Static_Files/MyChallenges/)
Sample project from previous module added with all the topics discussed in this module.

## FAQs

**Q - Is Django a web server and a framework?**\
A - Yes and no. Django has a built-in web server that's used for development purposes. This web server is used when you run the web app locally, such as when debugging in Visual Studio. When you deploy to a web host, however, Django uses the host's web server instead. The wsgi.py module in the Django project takes care of hooking into the production servers.

## References
- [Python Django - The Practical Guide By Academind](https://www.udemy.com/course/python-django-the-practical-guide/)
