# Generated by Django 2.1.1 on 2018-09-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eccopc', '0009_auto_20180923_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialnumber',
            name='bios',
            field=models.FileField(blank=True, upload_to='sterowniki/bios/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='chipset',
            field=models.FileField(blank=True, upload_to='sterowniki/chipset/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='instrukcja',
            field=models.FileField(blank=True, upload_to='sterowniki/manual/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='lan',
            field=models.FileField(blank=True, upload_to='sterowniki/lan/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='other',
            field=models.FileField(blank=True, upload_to='sterowniki/inne/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='other2',
            field=models.FileField(blank=True, upload_to='sterowniki/inne2/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='other3',
            field=models.FileField(blank=True, upload_to='sterowniki/inne3/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='podrecznik',
            field=models.FileField(blank=True, upload_to='sterowniki/manual/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='sata',
            field=models.FileField(blank=True, upload_to='sterowniki/sata/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='security',
            field=models.FileField(blank=True, upload_to='sterowniki/sec/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='sound',
            field=models.FileField(blank=True, upload_to='sterowniki/dzwiek/'),
        ),
        migrations.AlterField(
            model_name='serialnumber',
            name='vga',
            field=models.FileField(blank=True, upload_to='sterowniki/vga/'),
        ),
    ]
