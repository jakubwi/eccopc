from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(blank=True, upload_to='category/')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self) .save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=125, unique=True)
    picture = models.ImageField(blank=True, upload_to='products/')
    body = RichTextUploadingField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self) .save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def __str__(self):
        return self.name