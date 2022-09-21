# Learn Django (for beginners)

## Introduction

Django is a Python-based web framework which allows you to quickly create web application without all of the installation or dependency problems that you normally will find with other frameworks. For more info, [click here](https://www.geeksforgeeks.org/django-basics/)

**Other useful readings**

- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [W3Schools](https://www.w3schools.com/django/index.php)
- [My Notes](other/Django.pdf)

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
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## URLs and Views

### 1. URL
![url academind slide image](other/images/urls_and_views/urls.png)

Readings:
- [Techvidvan - Django URLs and URL Mapping](https://techvidvan.com/tutorials/django-urls/)
- [Offical Django Docs - URL Dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

### 2. Views
![views academind slide image](other/images/urls_and_views/views-1.png)

![views academind slide image](other/images/urls_and_views/views-2.png)

![request and response academind slide image](other/images/urls_and_views/request_and_response.png)

Readings:
- [The Django Book - Mastering Django: Views](https://djangobook.com/django-tutorials/mastering-django-views/)

### [3. Monthly Challenges Project](01-URLs_and_Views/MyChallenges/)

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

- Please check the implementation about the template renders here, [views.py](02-Templates_and_Static_Files/MyChallenges/challenges/views.py) to know about rendering of templates.

### 2. Django Template Language

![DTL academind slide image](other/images/urls_and_views/dtl.png)

### 3. Filters

Readings:
- [GeeksforGeeks - Django Template Filters](https://www.geeksforgeeks.org/django-template-filters/#:~:text=Django%20Template%20Engine%20provides%20filters,it%20to%20one's%20own%20need.)
- [Official Docs - Built-in template tags and filters](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

Why Filter?\
You want to limit the work you do in the view and really restrict it to your core business logic which might be needed for fetching and transforming the data and when it comes to formatting and outputting the data you might wanna do as much of that logic in the template and filters are a great tool for that.

### 4. Tags

Readings:
- [GeeksforGeeks - Django Template Tags](https://www.geeksforgeeks.org/django-template-tags/)

[for](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#for) and [url](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#url) tags usage can be seen here, [index.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) and for [if](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#if), refer [challenge_page.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html)

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

Check out the [parent template(base.html)](02-Templates_and_Static_Files/MyChallenges/templates/base.html) and how [index.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) & [challenge_page.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html) are extending parent template.

### 6. Including Partial Template Snippets

When we have HTML snippets which needs to be used by some templates but not all the templates, in that case, we can make use of **_include_** tag.

An example could be navigation bar. In a big website, there might be few pages which may used same navigation bar.

This can be implement at app level. In our example, we will create a nav bar which will redirect us to the 'challenges' route. Implementation can be see here, [header.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/includes/header.html) and [challenge_page.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/challenge_page.html). A directory 'includes'(you can give any other name as well) is created inside 'templates' dir in challenges app and inside that _header.html_ is created.  

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

Check out the implementation at [views.py](02-Templates_and_Static_Files/MyChallenges/challenges/views.py)

In our example project, if user hit URL which does not exist, we will get below 404 and not the template created for it. In order to render our 404 template, we need to set ***DEBUG=False*** in _settings.py_, however, with that, Django development web server will not start. Our 404 page can be render when we deploy our application.

![404 academind screenshot](other/images/urls_and_views/404.png)


### 9. Adding Static Files

Readings:
- [Official Docs - How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/4.0/howto/static-files/)
- [LearnDjango - Django Static Files and Templates](https://learndjango.com/tutorials/django-static-files)
- [Digital Ocean - Working with Django Templates & Static Files](https://www.digitalocean.com/community/tutorials/working-with-django-templates-static-files)

Checkout implementation of static files at app level here, [index.html](02-Templates_and_Static_Files/MyChallenges/challenges/templates/challenges/index.html) (css file, [challenges.css](02-Templates_and_Static_Files/MyChallenges/challenges/static/challenges/challenges.css) is added at app level at path <app_name>/static/<app_name>/<css_file>)

Static file implementation at global level can be find here, [base.html](02-Templates_and_Static_Files/MyChallenges/templates/base.html). To let Django know about global level static files ensure defining a list of directories (**STATICFILES_DIRS**) in your settings ([settings.py](02-Templates_and_Static_Files/MyChallenges/MyChallenges/settings.py)) file where Django will also look for static files.

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

### [10. Monthly Challenges Project](02-Templates_and_Static_Files/MyChallenges/)
Sample project from previous module added with all the topics discussed in this module.

## Data & Models

### 1. Introduction

Until now, we were storing our data either in file or assigning to some variables. However, data's persistent life is only till our servers are up and if servers are restarted, then all data would be vanished. Hence, we need database to store our data which is a more permanent solution.

Now to interact with databases, Django uses **models**.

### 2. Different Kinds of Data

![kind of data academind slide image](other/images/data_and_models/kinds_of_data.png)

### 3. Understanding Database options

![database options academind slide image](other/images/data_and_models/understanding_db_options.png)

>***Django has great built in support for a SQL, however, to use Django with NoSQL you will need to install extra packages.***

Readings:
- [SQL vs NoSQL](https://academind.com/tutorials/sql-vs-nosql)

### 4. Understanding SQL

When you creates a Django project, a [SQLite](https://www.sqlite.org/index.html) database is created with name **db.sqlite3**. If not, you can create a new file and simply name it db.sqlite3

![sql academind slide image](other/images/data_and_models/understanding_sql.png)

Above are some examples of SQL queries which shows the creation of table and inserting data into it. However, with Django, we can altogether avoid writing queries by using Models.

### 5. Django Models

Django models are classes that represent a table or collection in our Database. It contains all the information regarding the table. These models are stored together in Django in a file **models.py** in our Django App.

![django models academind slide image](other/images/data_and_models/django_models.png)

Readings:
- [Official Docs](https://docs.djangoproject.com/en/4.1/topics/db/models/)
- [Django Models - Ask Python](https://www.askpython.com/django/django-models)
- [GeeksforGeeks](https://www.geeksforgeeks.org/django-models/)

### 6. Creating a Django Model with Fields

You will find the **models.py** in Django apps and that's where we define our models.

For example:

```
from django.db import models

class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
```

Readings:
- [Django Model Fields - Official Docs](https://docs.djangoproject.com/en/4.1/ref/models/fields/)

### 7. Migrations

To make use of Django Model for creating table in database, we need to:

- First ensure our app is registered in **settings.py**.

- Secondly, database configurations are updated in **settings.py**.

- Now, in order to tell Django that it should reach out to the configured database, we will use the concept called [Migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/#:~:text=Migrations%20are%20Django's%20way%20of,problems%20you%20might%20run%20into.)

- Migrations needs to be executed every time model is updated.

We will use the Model shown in previous example for creating table in database based on it. For that, we will first run ***makemigrations*** command:

```
python3 manage.py makemigrations

Migrations for 'book_outlet':
  book_outlet/migrations/0001_initial.py
    - Create model Book
```

***makemigrations*** basically generates the SQL commands for preinstalled apps (which can be viewed in installed apps in settings.py) and your newly created app's model which you add in installed apps. It does not execute those commands in your database file. So tables are not created after ***makemigrations***.

After applying ***makemigrations*** you can see those SQL commands with ***sqlmigrate*** which shows all the SQL commands which have been generated by ***makemigrations***.

```
python3 manage.py sqlmigrate book_outlet 0001

BEGIN;
--
-- Create model Book
--
CREATE TABLE "book_outlet_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "rating" integer NOT NULL);
COMMIT;
```

Let's run ***migrate*** command.

```
python3 manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying book_outlet.0001_initial... OK
  Applying sessions.0001_initial... OK
```

You see above that other than initial migration, couple of other migrations are also applied. Reason being, this is the first time ***migrate*** command is executed and all these other migrations belongs to the other installed apps.

### 8. Inserting Data

Now that, tables are created in the database, we will try to insert some data in it.

We will first use Django shell to perform data insert operation and afterwards, we will see how same can be implemented with **views**.

- To open Django shell, type below command:

  ```
  python3 manage.py shell

  Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52)
  [Clang 6.0 (clang-600.0.57)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>>
  ```

  Interactive shell will get open.

- Import *Book* model class from app *book_outlet*. Object of *Book* class will denotes row in the DB table.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> harry_potter = Book(title="Harry Potter - Philospher's Stone", rating=5)
  >>>
  ```

- ***However, remember, by creating the object of model class will not create the entry in database.***

- To update the entry in database, we'll have to use **Model** class method called **save()** on Book class object which behind the scenes construct the SQL query and execute for us. Remember, **Book** class is inheriting **Model** class and **save()** method is defined in it.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> harry_potter = Book(title="Harry Potter - Philospher's Stone", rating=5)
  >>> harry_potter.save()
  >>> got = Book(title="Song of Ice and Fire", rating=5)
  >>> got.save()
  >>>
  ```

### 9. Getting all Entries

- To see the data saved by us, we can query database. For that, we have to use a **Model** class static attribute **objects**.

- Now, with the use of **objects** attribute with our own Model class, we get an object and on that, several methods can be used.

- [all()](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#all) is one of them which gives all of the data stored in the database. 

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> Book.objects.all()
  <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
  >>>
  ```

### 10. Updating Models and Migrations

In this section, we will see how the model class can be updated.

In our existing example, let's make 2 changes:

1. Define \_\_str\_\_ to print more user friendly instance name instead of default.
2. Add more fields.

First task can be achieved as below:

```
from django.db import models

# Create your models here.

class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
```

**Output**

```
>>> from book_outlet.models import Book
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>]>
>>>
```
Remember, in this task, we didn't change the class structure and just added a new special method. This means, we don't have to run ***makemigrations*** and ***migrate*** commands.

Now, let's add few fields and thereby, begin with 2nd task.

- We will add validators in rating field to make sure min and max value will not less than 1 and more than 5 respectively.
- Add new fields, *author* and *is_bestselling*

```
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.CharField(max_length=100)
    is_bestselling = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
```

Since, we have restructured our model class, therefore, to update the same in database, we need to run ***makemigrations*** and ***migrate*** commands. Let's do it.

```
python manage.py makemigrations

It is impossible to add a non-nullable field 'author' to book without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 
```

Here, we are getting this prompt because we are trying to add a non-nullable field *author* to *Book* without a default value and we already have some data in our database which up to this point, before we run these migrations, only have *title* and *rating* fields. So, now Django is basically asking what do you want to do for those new columns which you're adding, because by default, they're not allowed to be empty (That's what non-nullable means).

Let's select option 2 and fix it at code level.

```
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
```

Setting **null=True** means that if there is no value provided to *author* field, **null** will be assigned.

Let's run again ***makemigrations*** and ***migrate*** commands.

```
python manage.py makemigrations
Migrations for 'book_outlet':
  book_outlet/migrations/0002_book_author_book_is_bestselling_alter_book_rating.py
    - Add field author to book
    - Add field is_bestselling to book
    - Alter field rating on book

python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
Running migrations:
  Applying book_outlet.0002_book_author_book_is_bestselling_alter_book_rating... OK
```

Let's check out those changes

```
>>> from book_outlet.models import Book
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>]>
>>>
>>> Book.objects.all()[1].author
>>> Book.objects.all()[1].is_bestselling
False
>>>
>>> alchemist = Book(title="The Alchemist", rating=4, author="Paulo Coelho", is_bestselling=True)
>>> alchemist.save()
>>> Book.objects.all()[2].title
'The Alchemist'
>>>
>>> Book.objects.all()[2].author
'Paulo Coelho'
>>>
```

### 11. Blank vs Null

![blank vs null academind slide image](other/images/data_and_models/blank_vs_null.png)

### 12. Updating Data

Let's carry on with our previous example and update the value of *author* and *is_bestselling* fields for initially created entries.

```
>>> from book_outlet.models import Book
>>>
>>> hp = Book.objects.all()[0]
>>> hp.author = "J.K. Rowling"
>>> hp.is_bestselling = True
>>> hp.save()
>>>
>>> Book.objects.all()[0].author
'J.K. Rowling'
>>>
>>> Book.objects.all()[0].is_bestselling
True
>>>
>>> got = Book.objects.all()[1]
>>> got.author = "George R.R. Martin"
>>> got.is_bestselling = True
>>> got.save()
>>>
>>> Book.objects.all()[1].author
'George R.R. Martin'
>>>
>>> Book.objects.all()[1].is_bestselling
True
>>>
```

Readings:
- [Bulk Update](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-update)

### 13. Deleting Data

To delete the entry in database, we use **Model** class method **delete()**. See the usage below:

```
>>> from book_outlet.models import Book
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Alchemist (4)>]>
>>>
>>> alchemist = Book.objects.all()[2]
>>> alchemist.delete()
(1, {'book_outlet.Book': 1})
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>]>
>>>
```

Readings:
- [Bulk Delete](https://docs.djangoproject.com/en/4.1/topics/db/queries/#deleting-objects)

### 14. 'create' instead of 'save'

Till now, we have seen that to create an entry in database, first object of model class is created and then **save()** method is used to save it in the database. However, with the usage of **create()** method, we can avoid the step of creating object altogether. See the usage below:

```
>>> from book_outlet.models import Book
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>]>
>>>
>>> Book.objects.create(title="Half Girlfriend", rating=4, is_bestselling=False, author="Chetan Bhagat")
<Book: Half Girlfriend (4)>
>>>
>>> Book.objects.create(title="The Immortals of Meluha", rating=5, is_bestselling=True, author="Amish Tripathi")
<Book: The Immortals of Meluha (5)>
>>>
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: Half Girlfriend (4)>, <Book: The Immortals of Meluha (5)>]>
>>>
```

Readings:
- [Bulk Create](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)

### 15. Querying and Filtering Data

- In our example, up to this point if we wanted to get a desired book, we always used **objects.all()** and then an index of our desired book. It definitely works but it could also fail if we try to find some book which does not exist.

- It is not ideal as every time we have to memorize the index.

- Instead of this, it would be nicer if we could simply get our desired book by telling Django for which field to filter or if we could get a list of books that fulfill a certain condition.

- To achieve that, we can use [get()](https://docs.djangoproject.com/en/dev/ref/models/querysets/#get) or [filter()](https://docs.djangoproject.com/en/dev/ref/models/querysets/#filter)

Let's see the usage of both:

<ins><strong>get()</strong></ins>

- Returns the object matching the given lookup parameters, which should be in the format described in [Field Lookups](https://docs.djangoproject.com/en/4.1/topics/db/queries/#field-lookups).

- It raises MultipleObjectsReturned if more than one object was found. The MultipleObjectsReturned exception is an attribute of the model class.

- It raises a DoesNotExist exception if an object wasn't found for the given parameters. This exception is also an attribute of the model class.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> Book.objects.get(id=1)
  <Book: Harry Potter - Philospher's Stone (5)>
  >>>
  >>> Book.objects.get(id=3)
  Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/models/manager.py", line 85, in manager_method
      return getattr(self.get_queryset(), name)(*args, **kwargs)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/models/query.py", line 496, in get
      raise self.model.DoesNotExist(
  book_outlet.models.Book.DoesNotExist: Book matching query does not exist.
  >>>
  >>> Book.objects.get(title="Half Girlfriend")
  <Book: Half Girlfriend (4)>
  >>>
  >>> Book.objects.get(is_bestselling=True)
  Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/models/manager.py", line 85, in manager_method
      return getattr(self.get_queryset(), name)(*args, **kwargs)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/models/query.py", line 499, in get
      raise self.model.MultipleObjectsReturned(
  book_outlet.models.Book.MultipleObjectsReturned: get() returned more than one Book -- it returned 3!
  ```

<ins><strong>filter()</strong></ins>

- Returns a new QuerySet containing objects that match the given lookup parameters.
- In methods like **filter, exclude, get**, etc, you cannot do comparing or other operations by using operators or you mostly do in Python. See example below where *rating<4* is used and a error was thrown.
- To do so, [Field Lookups](https://docs.djangoproject.com/en/4.1/topics/db/queries/#field-lookups) are used.
- Syntax for using field lookups is:

    ```
    field__lookuptype=value
    ```
- Find [here](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups) all different types of field lookups.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> Book.objects.filter(is_bestselling=True)
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> Book.objects.filter(is_bestselling=True, rating=5)
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> Book.objects.filter(rating<4)
  Traceback (most recent call last):
    File "<console>", line 1, in <module>
  NameError: name 'rating' is not defined
  >>>
  >>> Book.objects.filter(rating__gte=4, is_bestselling=False)
  <QuerySet [<Book: Half Girlfriend (4)>]>
  ```

> Basically use get() when you want to get a single unique object, and filter() when you want to get all objects that match your lookup parameters.

Readings:
- [Making Queries in Django - Official Docs](https://docs.djangoproject.com/en/4.1/topics/db/queries/)
- [get() vs filter()](https://stackoverflow.com/questions/3221938/difference-between-djangos-filter-and-get-methods)

### 16. "or" Conditions

- Up to this point, all those conditions we have written in previous section using **Field Lookups** are combined with **AND** operation, such as, if rating is greater than or equal to 4 and *is_bestselling* is False, give all such results.

- But what if I want to use combine these condition with **OR** operation. For that, Django provides ***Q*** class. See the usage of **Q** class below.

- In one of the example below, combination of **AND** and **OR** is used and condition separated with **AND** is comma-separated but enclosed in ***Q*** class. This is allowed. ***Remember, OR ones will be separated using **pipe(|)** and AND ones will separated using comma(,).***

- If you don't want to enclosed conditions with ***Q*** compared with **AND**, then, you have to write it at the very end. Refer example below.

  ```
  >>> from book_outlet.models import Book
  >>> from django.db.models import Q
  >>>
  >>> Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> Book.objects.filter(Q(rating__gt=4) | Q(is_bestselling=True))
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> Book.objects.filter(Q(rating__gt=4) | Q(is_bestselling=True), Q(author="J.K. Rowling"))
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>]>
  >>>
  >>> Book.objects.filter(Q(rating__gt=4) | Q(is_bestselling=True), author="J.K. Rowling")
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>]>
  >>>
  >>> Book.objects.filter(author="J.K. Rowling", Q(rating__gt=4) | Q(is_bestselling=True))
    File "<console>", line 1
      Book.objects.filter(author="J.K. Rowling", Q(rating__gt=4) | Q(is_bestselling=True))
                                                                                        ^
  SyntaxError: positional argument follows keyword argument
  >>>
  ```

### 17. Query Performance

When you run queries, you learnt that certain operations instantly hit the database whilst others don't. Let's understand with examples.

- In below example, you might be thinking that the database is queried and results are stored in variable "bestsellers" as soon as enter was hit. ***Please note that this isn't the case. Instead, after hitting the enter, "bestsellers" var only consists of Query definition***

- Database will be queried when "bestsellers" var will be printed or used otherwise.

  ```
  >>> bestsellers = Book.objects.filter(is_bestselling=True)
  >>> print(bestsellers)
  ```

- This can be helpful to chain your query definition and query database in efficient way. In below example, "bestsellers" and "amazing_bestseller" var has query definition and "amazing_bestseller" var is using "bestsellers" to chain query. Now, Django has a elegant way to perform this. It notices that "amazing_bestseller" is based on "bestsellers" and it actually caches the results of your query sets. Hence, showing efficient of querying database.

  ```
  >>> bestsellers = Book.objects.filter(is_bestselling=True)
  >>> amazing_bestseller = bestsellers.filter(rating__gt=4)
  >>> print(bestsellers)
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> print(amazing_bestseller)
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: The Immortals of Meluha (5)>]>
  ```

- If you find yourself writing some code where you need the results from different query sets, you might wanna structure your code such that you allow Django to reuse cashed results.

- In other scenario, if you have something like shown in below example, then every single time, database will be queried and it is not efficient as Django is not caching it and eventually not able to reuse it.

  ```
  >>> print(Book.objects.filter(rating__gt=3))
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: Half Girlfriend (4)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  >>> print(Book.objects.filter(rating__gt=3))
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: Half Girlfriend (4)>, <Book: The Immortals of Meluha (5)>]>
  >>>
  ```

### 18. Preparing Templates, Rendering Queried Data in the Templates, Rendering the Details page and Model URLs 

Now, we see how we can harness models and renders data in the templates from database via views.

Demonstrations includes:

- We will create a simple template where all books will be displayed.

- We will then make all book clickable to show more details.

- Please **base.html** will be created at app level in order to avoid writing more configurations.

Readings:
- [get_absolute_url()](https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url)
- [When to use Django get_absolute_url() method?](https://stackoverflow.com/questions/43179875/when-to-use-django-get-absolute-url-method)

### 19. Adding a SlugField & Overwriting save()

In this section, we will see the implementation of slug and necessities of overwriting **save()** method.

- In our example, when we click on a specific book, it is then redirecting us to that book details. To achieve it, **id** of that specific book is being used.

- However, when we see search engine point of view, it does not look nice.

- Let's see how to use slug here.

  - We don't necessarily need to replace our **id**, rather we can make use **SlugField** provided by Django which will store slugs specific to that book entry.

  - Now the next question is that how we generate slug for corresponding book automatically which follows some pattern, let's say, *song-of-ice-and-fire* which is based on our book title and separated by '-'.

  - To do that, we will first set the default value of **SlugField** as empty string and null as False. In that way, whenever a new book entry would be added, slug value will be an empty string and never a null.

  - But how can slug field be automatically updated for each newly added book?

  - To do that, we have to overwrite our **save()** method in a way that every time it is called to update database for some specific book entry, it will also save the slug field value for that book. Now to generate slugs, Django provide a method called **Slugify**. Check out below implementation.

  ```
  from django.db import models
  from django.core.validators import MinValueValidator, MaxValueValidator
  from django.utils.text import slugify

  class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
  ```

  - ***For the entries exists before these changes, we need to update slugs manually by running save() method.***

- After making all above changes, our database needs to updated. Hence, we have to execute ***makemigrations*** and ***migrate*** command.

  ```
  python3 manage.py makemigrations
  Migrations for 'book_outlet':
    book_outlet/migrations/0003_book_slug.py
      - Add field slug to book

  python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
  Running migrations:
    Applying book_outlet.0003_book_slug... OK
  ```

- Let's also update the slug field for existing fields by called **save()** method.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> Book.objects.all()
  <QuerySet [<Book: Harry Potter - Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: Half Girlfriend (4)>, <Book: The Immortals of Meluha (5)>]>
  >>> for i in Book.objects.all():
  ...     i.save()
  ...
  >>>
  >>> Book.objects.get(id=1).slug
  'harry-potter-philosphers-stone'
  >>>
  >>> Book.objects.get(id=2).slug
  'song-of-ice-and-fire'
  >>>
  >>> Book.objects.get(id=4).slug
  'half-girlfriend'
  >>>
  >>> Book.objects.get(id=5).slug
  'the-immortals-of-meluha'
  >>>
  ```

### 20. Using the Slug and Updating Field Options

To use slug to link book details, below updates are made:

[views.py](03-Data_and_Models/book_store/book_outlet/views.py)

```
def book_detail_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_details.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_bestseller': book.is_bestselling,
    })
```

[index.html](03-Data_and_Models/book_store/book_outlet/templates/book_outlet/index.html)

Added an entry to demonstrate slugs

```
<li><a href="{% url 'book-detail-slug' book.slug %}">{{ book.title }}</a> (Rating: {{ book.rating }}) - calling book detail page by using slugs</li>
```

[urls.py](03-Data_and_Models/book_store/book_outlet/urls.py)

Added this url which will execute slug based view.

```
path("<slug:slug>", views.book_detail_slug, name='book-detail-slug')
```

Consider that you are using slugs in your project and to ensure that whenever an user visits your site, find operation works quickly with slug. ***To do that, you make your slug field as 'database index'***. Just set **db_index** as **True** in your model class like below.

```
slug = models.SlugField(default="", null=False, db_index=True)
```

Database indexes are a technical detail of databases (SQL and NoSQL). It basically means that the database will save the values in that column a bit more efficiently or in a way that makes searching them a bit more efficient and that's some behind the scenes stuff which you don't need to know.

All you need to know is that creating such an index for a field can make searching that field quicker. So if you have a field which gets used a lot for finding data, like in our case, slug which we know to find books then we might wanna consider turning it into an index.

The ID field, which we get out of the box automatically has an index.

Now, you might think why don't we make every field an index if it speeds up the search performance, the problem is that creating an index on its own decreases performance because whenever you add a new entry to your database it needs to be added to the index, and if all your fields are indexes, that adds up. So having a few fields as indexes is no problem, but you definitely shouldn't turn all your fields into indexes really just the ones which you use a lot for querying.

Readings:
- [What is a Database Index?](https://www.codecademy.com/article/sql-indexes)

### 21. Aggregation and Ordering

<ins><strong>Aggregation</strong></ins>

Let's say on the index page we wanna show the total number of books which we have and also the average rating. How could we do that?

Well, thankfully, Django makes this very easy because it has something which is called aggregation methods. It has built-in methods which you can use on your models to aggregate results. See the usage below.

**views.py** - See how *tot_num_of_books* and *avg_rating* is used.

```
from django.db.models import Avg

def index(request):
    books = Book.objects.all()
    tot_num_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'tot_num_of_books': tot_num_of_books,
        'avg_rating': avg_rating,
    })
```

**index.html** - Adding these 2

```
<hr>
<p>Total Number of Books - {{ tot_num_of_books }}</p>
<p>Average Ratings - {{ avg_rating }}</p>
```

If you run this, you will find *avg_rating* has the value *{rating__average}* which is a dictionary. This is because *aggregate* method can accept multiple functions and value of each those functions returned in a dictionary with syntax as <function_name>__<model_field_name>.

<ins><strong>Ordering</strong></ins>

Sorting is also a very simple with Django. For that, you can use [order_by()](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#order-by). It allows you to order the results in the query set and it will do the ordering on the database level so that you need not to do it using Python. See the usage below.

```
def index(request):
    books = Book.objects.all().order_by('title')
```

By default, it sorts in ascending order. To sort in descending order, just add **"-"** before the field name.

```
def index(request):
    books = Book.objects.all().order_by('-title')
```

### Here's the [book_store](03-Data_and_Models/book_store/) project

## Admin

### 1. Introduction

- Previously, we have seen interaction of database with Django via model and used interactive Django shell to perform many database related operations using Django concepts.

- While this is something we can do but as the site owner it's really not convenient because if your app is running on production server, you would not want to first login to that server, activate the shell and then perform operations.

- The better approach would be to have some graphical interface exposed which can be used for same purpose. We can definitely build something like that, however, Django already provides built in administration user interface to administer your data.

### 2. Logging Data into the Admin Panel

- If you go to the [urls.py](03-Data_and_Models/book_store/book_store/urls.py), you will find **admin/** url. This is where ***Django Administration*** interface is exposed.

- This ***Django Administration*** interface is part of **django.contrib.admin** app and it comes builtin with Django.

- ***Remember, this administration interface is not meant for the end users or visitors of your site but for you as the site owner to administer the contents that makes up your site.***

- Now, to use this administration interface, you need to create a superuser account. For that, run below command:

  ```
  python3 manage.py createsuperuser
  Username (leave blank to use 'aman'): aman
  Email address: test@test.com
  Password:
  Password (again):
  Superuser created successfully.
  ```

- Once credentials are created, start your local server and go to ```localhost:8000/admin``` and use your credentials to login.

- Once logged in and if you are looking for data related to your model and it is not there then follow the next section for the reason.

### 3. Adding Models to the Admin Area

- To access data related to your models in ***Django Administration*** page, you need to make Django aware about it because not necessarily all your models need to be managed here.

- If some content is user generated and you as an admin might not need to moderate or view it then you might not wanna include it here.

- Therefore, you have to explicitly inform Django about which data should show up here.

- To make Django aware, we need to make some changes in **admin.py**. See code snippet below.

  ```
  from django.contrib import admin
  from .models import Book

  # Register your models here.

  admin.site.register(Book)
  ```

- If now the server is restarted, **Book** model will be appeared.

### 4. Configuring Model Fields

- In above section, we have successfully added our **Book** model to admin UI.

- With that, CRUD operations can be performed easily.

- In our example, with current implementation, if we try to add new book and left slug field empty (because during save, it will automatically populated, so why bother?) then the entry will not be created as slug field is required one. So, how can it be resolved?

- One workaround is to add ```blank=True``` in **SlugField()**. With that, you can save without updating slug field and it will be updated automatically during save.

  ```
  slug = models.SlugField(default="", null=False, blank=True,db_index=True)
  ```

- Another workaround is add ```editable=False``` in **SlugField()**. With that, this field will become uneditable in Django admin UI.

  ```
  slug = models.SlugField(default="", null=False, editable=False ,db_index=True)
  ```

- However, as the best practice, we may want to show this field as uneditable and have the slug data prefilled. ***But to do that, We have to customize our administration area other than adding more and more arguments here at model level. Remember, arguments on the slug field(or any other field in Django model otherwise) are mostly there to configure the settings for the database.***

### 5. Configuring the Admin Settings

Continuing from where we've left:

- Field's appearance on Django admin UI page can be configured by introducing changes at **admin.py** module level. We can make use of [ModelAdmin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-objects) class.

  ```
  from django.contrib import admin
  from .models import Book

  # Register your models here.

  class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

  admin.site.register(Book, BookAdmin)
  ```

- Above will achieve what we want. However, if there is requirement to make some field uneditable, then [readonly_fields](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields) can be used.

Readings:
- [Django Admin - Official Docs](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)

### 6. More Config Options

- [list_filter](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter)
- [list_display](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

Added both in our configuration.

```
from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)

admin.site.register(Book, BookAdmin)
```

**Output**

![config options personal project image](other/images/admin/config_options.png)

### Here's the [book_store](03-Data_and_Models/book_store/) project with updated Django Admin UI interface code

## Relationships

### 1. Introduction

- To this point, we have only worked with one model, more specifically, the **Book** model but in real world websites, you will have more than one data entity. For example, we can have **author** as separate data entity (model) although we have a **author** field in **Book** model, however, it is hard coded text.

- We might want to store **author** as separate data entities to ensure that we don't try to add *Max* (author name) to two different books, one time as 'Max' and another time as 'Maximilian' which are actually the same author, but typed differently.

- Therefore, in this module, we will learn about relationships between data entities.

### 2. Understanding Relationship Type

![relationship types academind slide image](other/images/relationships/1_relationships_types.png)

![relationship types academind slide image](other/images/relationships/2_relationships_types.png)

Readings:
- [Relationship in Django Model - Official Docs](https://docs.djangoproject.com/en/4.1/topics/db/examples/)

### 3. Adding one-to-many Relation & Migrations

- Let's continue with our **Book Store** project and create separate model for **author** field (eventually separate table for **author** in database) and established one to many relationship. In this case, **Author** will be unique and **Book** can be multiple, so **Author** represents *one* and **Book** represents *many*.

  <ins><strong>Model Class for Author</strong></ins>

  ```
  from django.db import models

  class Author(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
  ```

- To connect **Author** model with **Book** model, we will add [ForeignKey](https://zerotobyte.com/complete-guide-to-django-foreignkey/#:~:text=What%20is%20ForeignKey%20in%20Django,to%20connect%20data%20using%20ForeignKeys.). With that, instead of directly inserting the **author** data in the field, we point at another database entry in another table and Django will set up that pointer to be stored in the database and manage that connection for us behind the scenes. In our case, we just need to let Django know that we want to connect our **Book** model with **Author** for **author** field. Below is the implementation:

  ```
  from django.db import models
  from django.core.validators import MinValueValidator, MaxValueValidator

  class Book(models.Model):

      # Class attributes define schema
      title = models.CharField(max_length=50)
      rating = models.IntegerField(
          validators=[
              MinValueValidator(1),
              MaxValueValidator(5)
          ]
      )
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      is_bestselling = models.BooleanField(default=False)
      slug = models.SlugField(default="", null=False, db_index=True)
  ```

  > ***Side Note:***
  >
  > ***To define a relationship between two models, you need to define the ForeignKey field in the model from the Many side of the relationship.  In other words, ForeignKey should be placed in the Child table, referencing the Parent table.***

- Now, we have save those changes in database and for that, we need to run ***makemigrations*** and ***migrate*** commands.

  ```
  python3 manage.py makemigrations
  It is impossible to change a nullable field 'author' on book to non-nullable without providing a default. This is because the database needs something to populate existing rows.
  Please select a fix:
  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
  2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
  3) Quit and manually define a default value in models.py.
  Select an option:
  ```

- While running ***makemigrations***, we get warning here because we are trying to change the **author** field and that too as non-nullable and without default value. It's complaining about that because the old author database column basically has to be thrown away and replaced with the new one as the old author column had string entries. Let's choose the option 3 and correct the code by ```null=True``` in **author** field and run again the ***makemigrations*** command which results in successful result.

  ```
  python3 manage.py makemigrations
  Migrations for 'book_outlet':
  book_outlet/migrations/0004_author_alter_book_author.py
    - Create model Author
    - Alter field author on book
  ```

- With that, if we now run ***migrate*** command, the new issue will be found which is related to the existing **author** field. Since type of the **author** field has been changes but in our database, for the existing entries, **author** field has string value. So, there's a conflict and due to which the error.

  ```
  python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
  Running migrations:
    Applying book_outlet.0004_author_alter_book_author...Traceback (most recent call last):
    File "/Users/aman/Documents/Git_Repos/learningDjango/04-DB_Relationships/book_store/manage.py", line 22, in <module>
      main()
    File "/Users/aman/Documents/Git_Repos/learningDjango/04-DB_Relationships/book_store/manage.py", line 18, in main
      execute_from_command_line(sys.argv)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
      utility.execute()
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/__init__.py", line 440, in execute
      self.fetch_command(subcommand).run_from_argv(self.argv)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/base.py", line 414, in run_from_argv
      self.execute(*args, **cmd_options)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/base.py", line 460, in execute
      output = self.handle(*args, **options)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/base.py", line 98, in wrapped
      res = handle_func(*args, **kwargs)
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/core/management/commands/migrate.py", line 290, in handle
      post_migrate_state = executor.migrate(
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/migrations/executor.py", line 131, in migrate
      state = self._migrate_all_forwards(
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/migrations/executor.py", line 163, in _migrate_all_forwards
      state = self.apply_migration(
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/migrations/executor.py", line 251, in apply_migration
      migration_recorded = True
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/backends/sqlite3/schema.py", line 37, in __exit__
      self.connection.check_constraints()
    File "/Users/aman/Documents/Git_Repos/learningDjango/.venv/lib/python3.9/site-packages/django/db/backends/sqlite3/base.py", line 383, in check_constraints
      raise IntegrityError(
  django.db.utils.IntegrityError: The row in table 'book_outlet_book' with primary key '1' has an invalid foreign key: book_outlet_book.author_id contains a value 'J.K. Rowling' that does not have a corresponding value in book_outlet_author.id.
  ```

- To avoid such type of issues, best practice is to design your model ahead of time, however, since, here we are in learning phase, it is good to be aware about it.

- Now about fixing, we can activate the shell and manually delete all entries from table corresponding **Book** model and then run ***migrate*** command again.

  ```
  >>> from book_outlet.models import Book
  >>>
  >>> Book.objects.all().delete()
  (5, {'book_outlet.Book': 5})
  >>>
  ```

  ```
  python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
  Running migrations:
    Applying book_outlet.0004_author_alter_book_author... OK
  ```

### 4. Working with Relations in Python Code

Let's add some data using our models **Book** and **Author** and for that, we will make use of *Django shell*.

```
>>> from book_outlet.models import Book, Author
>>>
>>> jkr = Author(first_name='J.K.', last_name='Rowling')
>>> jkr.save()
>>> Author.objects.all()
<QuerySet [<Author: Author object (1)>]>
>>> Author.objects.all()[0].first_name
'J.K.'
>>>
>>> Author.objects.all()[0].first_name
'J.K.'
>>> bk1 = Book(title="Harry Potter - The Philospher's Stone", rating=5, author=jkr, is_bestselling=True, slug="")
>>> bk1.save()
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
>>> Book.objects.all()[0].author
<Author: Author object (1)>
>>> Book.objects.all()[0].author.first_name
'J.K.'
>>> Book.objects.all()[0].author.last_name
'Rowling'
>>> Book.objects.all()[0].slug
'harry-potter-the-philosphers-stone'
>>>
```

### 5. Cross Model Queries

In previous section, we discussed about inserting data and verify the relationship between them. Now, we will see how the data of other model can be accessed from another and vice versa.

<ins><strong>From Book model (Many)</strong></ins>

In our case, **Book** model represents *many* in terms of relationship and to get the **author** information which is there in separate table, you can use below syntax:

```
<model_name_with_one_relationship>__<model_name_field_name>
```

If you want to further add field lookups with it, you can do it below manner:

```
<model_name_with_one_relationship>__<model_name_field_name>__<field_lookup>
```

***Examples***

```
>>> books_by_rowling = Book.objects.filter(author__last_name="Rowling")
>>> books_by_rowling
<QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
>>>
>>> books_by_rowling = Book.objects.filter(author__last_name__icontains="Row")
>>> books_by_rowling
<QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
>>>
```

<ins><strong>From Author model (One)</strong></ins>

In scenario where we want to query from **Author** model to find out all the books related to it, it can be done in 2 ways:

- *By using default attribute which has the below syntax:*

  ```
  <model_name_with_many_relation_all_in_lowercase>_set
  ```

  ***Examples***

  ```
  >>> from book_outlet.models import Book, Author
  >>>
  >>> jkr = Author.objects.get(first_name="J.K.")
  >>> jkr
  <Author: Author object (1)>
  >>> jkr.book_set
  <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f8919376910>
  >>> jkr.book_set.all()
  <QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
  >>> jkr.book_set.filter(is_bestselling=True)
  <QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
  >>> jkr.book_set.all()[0].slug
  'harry-potter-the-philosphers-stone'
  >>>
  ```

- *By using custom created name for Model class with many relation*. This name is created using the [related_name](https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.related_name) argument in *ForeignKey*

> If you’d prefer Django not to create a backwards relation, set related_name to '+' or end it with '+'. For example, this will ensure that the User model won’t have a backwards relation to this model:
>
> user = models.ForeignKey(
>    User,
>    on_delete=models.CASCADE,
>   related_name='+',
> )
>

Updating Model

```
from django.db import models

class Book(models.Model):

  # Class attributes define schema
  title = models.CharField(max_length=50)
  rating = models.IntegerField(
      validators=[
          MinValueValidator(1),
          MaxValueValidator(5)
      ]
  )
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books" ,null=True)
  is_bestselling = models.BooleanField(default=False)
  slug = models.SlugField(default="", null=False, db_index=True)
```

Next, run ***makemigrations*** and ***migrate*** commands:

```
python3 manage.py makemigrations
Migrations for 'book_outlet':
  book_outlet/migrations/0005_alter_book_author.py
    - Alter field author on book

python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
Running migrations:
  Applying book_outlet.0005_alter_book_author... OK
```

Let's test it out:

```
>>> from book_outlet.models import Book, Author
>>>
>>> jkr = Author.objects.get(first_name="J.K.")
>>> jkr.books.all()
<QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
>>> jkr.books.get(is_bestselling=True)
<Book: Harry Potter - The Philospher's Stone (5)>
>>> jkr.books.filter(rating__gte=4)
<QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
>>>
```

Readings:
- [What are related_name used for?](https://stackoverflow.com/questions/2642613/what-is-related-name-used-for)

### 6. Managing Relations in Admin

In this section, let's see how we can perform CRUD operations executed previously in Django Admin UI now.

- Let's register first our **Author** model. See below the updated **admin.py** from **book_outlet** app.

  ```
  from django.contrib import admin
  from .models import Book, Author

  # Register your models here.

  class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")

  admin.site.register(Book, BookAdmin)
  admin.site.register(Author)
  ```

- And also update the **Author** model in order to display user friendly name for **author** field.

  ```
  from django.db import models

  class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
  ```

- Go to ```localhost:8000/admin/```, and entries for both **Author** and **Book** like below:

  <ins><strong>Author</strong></ins>

  ![author entry personal project image](other/images/relationships/author_entry.png)

  <ins><strong>Book</strong></ins>

  ![author entry personal project image](other/images/relationships/book_entry.png)

### 7. Adding a one-to-one Relation

- To demonstrate one-to-one relation, we will create **Address** model and linked it with **Author** model.

- [OnetoOneField()](https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/) will be used to define **address** field in **Author** model.

- Logically, it will make more sense to define *OnetoOneField()* in **Author** than to **Address** model. However, in one-to-one relationship, you can define *OnetoOneField()* field in any one of them (but go with one which make more sense logically).

- To ensure backward compatibility during ***makemigrations*** and ***migrate***, we will set ```null=True``` in *address* field.

- For one-to-one relations, ```related_name``` argument can also be used, however, Django will create by default a related name with same as of class (all in lowercase) in which *OnetoOneField()* is used. In this case, *author* related name will be created for reverse query. In case, you don't want to use same name, then you can define ```related_name``` argument.

  ```
  from django.db import models

  class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    postal = models.CharField(max_length=6)

  class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
  ```

- Let's run ***makemigrations*** and ***migrate*** command.

  ```
  python3 manage.py makemigrations
  Migrations for 'book_outlet':
  book_outlet/migrations/0006_address_author_address.py
    - Create model Address
    - Add field address to author

  python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
  Running migrations:
    Applying book_outlet.0006_address_author_address... OK
  ```

- Let's add address to our existing fielding.

  ```
  >>> from book_outlet.models import Author, Address, Book
  >>>
  >>> Author.objects.all()
  <QuerySet [<Author: J.K. Rowling>, <Author: George R.R. Martin>, <Author: Amish Tripathi>, <Author: Chetan Bhagat>, <Author: Ajay K. Pandey>]>
  >>> Author.objects.all()[0].address
  >>> addr1 = Address(street="1st Main Street", postal="123456", city="London")
  >>> addr2 = Address(street="2nd Main Street", postal="789101", city="Mumbai")
  >>> addr1.save()
  >>> addr2.save()
  >>> jkr = Author.objects.get(first_name="J.K.")
  >>> jkr.address
  >>> jkr.address = addr1
  >>> jkr.save()
  >>> jkr.address
  <Address: Address object (1)>
  >>> jkr.address.street
  '1st Main Street'
  >>>
  >>> Address.objects.all()[0].author
  <Author: J.K. Rowling>
  >>>
  >>> Address.objects.all()[0].author.first_name
  'J.K.'
  >>> Address.objects.all()[0].author.last_name
  'Rowling'
  >>>
  ```

### 8.One-to-one & Admin Config

- Let's register **Address** model in Django Admin UI interface and start server.

  **admin.py**

  ```
  from django.contrib import admin
  from .models import Book, Author, Address

  # Register your models here.

  class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")

  class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

  admin.site.register(Book, BookAdmin)
  admin.site.register(Author, AuthorAdmin)
  admin.site.register(Address)
  ```

- Let's also add **\_\_str\_\_()** method to display the more user friendly **Address** model object names.

  ```
  def __str__(self):
    return f"{self.street}, {self.city}, {self.postal}"
  ```

- After logging to *admin* page, everything seems fine expect for the format of **Address** model is showing up.

  ![admin page personal project image](other/images/relationships/admin_page.png)

- To fix this, we will use the Python concept of class within class which is also used by Django for metadata operations. Below is the implementation:

  ```
  class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    postal = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = "Address Entries"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal}"
  ```

Readings:
- [verbose_name_plural](https://docs.djangoproject.com/en/4.1/ref/models/options/#verbose-name-plural)
- [Model Meta Options](https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options)

### 8. Setting up many to many

- To demonstrate many-to-many relation, we will create **Country** model and linked it with **Book** model. So, basically, we mean, a book can be published in many counteries and a country can publish many books.

- Let's create **Country** model for it.

  ```
  class Country(models.Model):
      name = models.CharField(max_length=80)
      code = models.CharField(max_length=2)
  ```

- [ManytoManyField()](https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/#many-to-many-relationships) is used to create many to many relation and a field using this can be defined in either of the model going for many-to-many relation, however, this should be define in the model where it makes sence logically. Hence, in our case, define *ManytoManyField()* in **Book** model. Below is the updated **Book** model class.

  ```
  from django.db import models

  class Book(models.Model):

    # Class attributes define schema
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books" ,null=True)
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country)
    slug = models.SlugField(default="", null=False, db_index=True)
  ```

- In *ManytoManyField()*, **on_delete** argument is not available and that's one of the difference among other two kinds of relations.

- To maintain a many-to-many relationship between two tables in a database, the only way is to have a third table which has references to both of those tables. This table is called a ***through*** table and each entry in this table will connect the source table and the target table. This is exactly what Django does under the hood when you use a ManyToManyField. It creates a through model which is not visible to the ORM user.

- After these changes, run ***makemigrations*** and ***migrate*** command

  ```
  python3 manage.py makemigrations
  Migrations for 'book_outlet':
  book_outlet/migrations/0007_country_alter_address_options_and_more.py
    - Create model Country
    - Change Meta options on address
    - Add field published_countries to book

  python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
  Running migrations:
    Applying book_outlet.0007_country_alter_address_options_and_more... OK
  ```

- Let's begin with updating data in models using Django shell.

  ```
  >>> from book_outlet.models import Book, Author, Address, Country
  >>>
  >>> Book.objects.all()
  <QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>, <Book: Song of Ice and Fire (5)>, <Book: Half Girlfriend (4)>, <Book: The Immortals of Meluha (5)>, <Book: You are the best friend (3)>]>
  >>>
  >>> book1 = Book.objects.all()[0]
  >>> book1.published_countries
  <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7fcd2129df40>
  >>>
  >>> book1.published_countries.all()
  <QuerySet []>
  >>>
  >>> ind = Country(name="India", code="IN")
  >>> uk = Country(name="United Kingdom", code="UK")
  >>> ind.save()
  >>> uk.save()
  ```

- Above, only **Country** model was updated with data. Now, to link this data with **Book** model, we cannot do like, ```book1.published_countries = uk```. Since *published_countries* is a list of countries which is holding a pointer to a another table. So, this wouldn't make sense because you must not forget that it's a many-to-many relation, hence it's not just one country which is related to this book. So setting this equal would be wrong.

- We will use a method called [add()](https://docs.djangoproject.com/en/4.1/ref/models/relations/#django.db.models.fields.related.RelatedManager.add) to add data in *published_countries*.

  ```
  >>> book1.published_countries.add(uk)
  >>> book1.published_countries.all()
  <QuerySet [<Country: Country object (2)>]>
  >>> book1.published_countries.filter(code="DE")
  <QuerySet []>
  >>> book1.published_countries.filter(code="UK")
  <QuerySet [<Country: Country object (2)>]>
  ```

- You can ofcourse query inverse, meaning, query **Country** model to find number of books associated with it. For that, we will make use of default field added by Django. So, in our case, inverse would be if we query from **Country** model, so the field would ```book_set```. It is similar as what we have seen in many-to-one relation. However, if you want to change the name of it, *related_name* argument use for it as we've seen before.

  ```
  >>> Country.objects.all()
  <QuerySet [<Country: Country object (1)>, <Country: Country object (2)>]>
  >>> c1 = Country.objects.all()[0]
  >>> c1.book_set.all()
  <QuerySet []>
  >>> c2 = Country.objects.all()[1]
  >>> c2.book_set.all()
  <QuerySet [<Book: Harry Potter - The Philospher's Stone (5)>]>
  >>>
  ```

Readings:
- [The right way to use a ManyToManyField in Django](https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django)
- [ManyToMany Relationship between two models in Django](https://stackoverflow.com/questions/61566808/manytomany-relationship-between-two-models-in-django)

### 9. Many-to-many in Admin

- Just like before, register **Country** model in **admin.py** and then login to Admin UI. Also, add meta class in **Country** model to fix the naming issue in Django Admin UI for **Country** model.

### 10. Circular Relations and Lazy Relations

- Sometimes, you might have two models that depend on each other - i.e. you end up with a circular relationship. Or you have a model that has a relation with itself. Or you have a model that should have a relation with some built-in model (i.e. built into Django) or a model defined in another application.

- Below, you find examples for all three cases that include Django's solution for these kinds of "problems": Lazy relationships. You can also check out the [official docs](https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields.related) in addition.

  - Two models that have a **circular relationship**

    ```
    class Product(models.Model):
      # ... other fields ...
      last_buyer = models.ForeignKey('User')

    class User(models.Model):
      # ... other fields ...
      created_products = models.ManyToManyField('Product')
    ```

    In this example, we have multiple relationships between the same two models. Hence we might need to define them in both models. By using the model name as a string instead of a direct reference, Django is able to resolve such dependencies.

  - Relation with the **same model**

    ```
    class User(models.Model):
      # ... other fields ...
      friends = models.ManyToManyField('self')
    ```

    The special self keyword (used as a string value) tells Django that it should form a relationship with (other) instances of the same model.

  - Relationships with **other apps** and their models (built-in or custom apps)

    ```
    class Review(models.Model):
      # ... other fields ...
      product = models.ForeignKey('store.Product') # '<appname>.<modelname>'
    ```

    You can reference models defined in other Django apps (no matter if created by you, via ```python manage.py startapp <appname>``` or if it's a built-in or third-party app) by using the app name and then the name of the model inside the app.

### Here's the [book_store](04-DB_Relationships/book_store/) project with relationship code updated in it

## FAQs

**Q - Is Django a web server and a framework?**\
A - Yes and no. Django has a built-in web server that's used for development purposes. This web server is used when you run the web app locally, such as when debugging in Visual Studio. When you deploy to a web host, however, Django uses the host's web server instead. The wsgi.py module in the Django project takes care of hooking into the production servers.

## References
- [Python Django - The Practical Guide By Academind](https://www.udemy.com/course/python-django-the-practical-guide/)
