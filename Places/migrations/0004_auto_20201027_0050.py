# Generated by Django 3.1.2 on 2020-10-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0003_auto_20201027_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(default=None, max_length=122),
        ),
    ]
