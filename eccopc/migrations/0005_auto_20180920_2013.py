# Generated by Django 2.1.1 on 2018-09-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0004_auto_20180920_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='products/category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
