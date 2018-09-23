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

class SerialNumber(models.Model):
    name = models.CharField(max_length=255, unique=False)
    sn = models.CharField(max_length=15, unique=False)
    gwarancja = models.CharField(max_length=55, unique=False, blank=True)
    instrukcja = models.FileField(upload_to='sterowniki/manual/', blank=True)
    podrecznik = models.FileField(upload_to='sterowniki/manual/', blank=True)
    bios = models.FileField(upload_to='sterowniki/bios/', blank=True)
    chipset = models.FileField(upload_to='sterowniki/chipset/', blank=True)
    sound = models.FileField(upload_to='sterowniki/dzwiek/', blank=True)
    vga = models.FileField(upload_to='sterowniki/vga/', blank=True)
    sata = models.FileField(upload_to='sterowniki/sata/', blank=True)
    lan = models.FileField(upload_to='sterowniki/lan/', blank=True)
    security = models.FileField(upload_to='sterowniki/sec/', blank=True)
    other = models.FileField(upload_to='sterowniki/inne/', blank=True)
    other2 = models.FileField(upload_to='sterowniki/inne2/', blank=True)
    other3 = models.FileField(upload_to='sterowniki/inne3/', blank=True)

    def __str__(self):
        return self.sn
