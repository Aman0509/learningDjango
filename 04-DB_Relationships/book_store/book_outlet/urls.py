from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:id>", views.book_detail, name='book-details'),
    path("<slug:slug>", views.book_detail_slug, name='book-detail-slug')
]
