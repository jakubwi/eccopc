# Generated by Django 2.1.1 on 2018-09-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0002_auto_20180920_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='picture',
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static/products/'),
        ),
    ]
