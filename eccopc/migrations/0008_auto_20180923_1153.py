# Generated by Django 2.1.1 on 2018-09-23 09:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0007_auto_20180921_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sn', models.CharField(max_length=15)),
                ('instrukcja', models.FileField(upload_to='')),
                ('podrecznik', models.FileField(upload_to='')),
                ('bios', models.FileField(upload_to='')),
                ('chipset', models.FileField(upload_to='')),
                ('sound', models.FileField(upload_to='')),
                ('vga', models.FileField(upload_to='')),
                ('sata', models.FileField(upload_to='')),
                ('lan', models.FileField(upload_to='')),
                ('security', models.FileField(upload_to='')),
                ('other', models.FileField(upload_to='')),
                ('other2', models.FileField(upload_to='')),
                ('other3', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]