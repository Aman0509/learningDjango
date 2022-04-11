from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:month>', views.month_int), # This will be triggered only when dynamically url is entered of int datatype
    path('<str:month>', views.month, name="month-str"), # Dynamic Path Segments
]
