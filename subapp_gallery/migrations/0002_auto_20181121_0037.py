# Generated by Django 2.1.2 on 2018-11-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='subapp_gallery/static/subapp_gallery/'),
        ),
    ]
