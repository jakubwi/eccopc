# Generated by Django 2.1.1 on 2018-09-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0003_auto_20180920_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media/products/thumb/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media/products/'),
        ),
    ]
