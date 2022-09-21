from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"
    
    def __str__(self):
        return f"{self.name} - {self.code}"

class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    postal = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = "Address Entries"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

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

    # Another way to creating url for book_detail view
    def get_absolute_url(self):
        return reverse("book-details", args=[self.id])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"