# Generated by Django 3.1.2 on 2020-10-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreePicturesApp', '0002_auto_20201016_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treepicture',
            name='picture',
            field=models.ImageField(upload_to='static/uploads/'),
        ),
    ]
