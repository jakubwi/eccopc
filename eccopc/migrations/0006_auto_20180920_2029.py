# Generated by Django 2.1.1 on 2018-09-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0005_auto_20180920_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='category/'),
        ),
    ]