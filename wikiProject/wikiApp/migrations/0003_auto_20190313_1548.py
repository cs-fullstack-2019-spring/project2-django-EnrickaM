# Generated by Django 2.2 on 2019-03-13 15:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wikiApp', '0002_auto_20190313_1524'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newuser',
            new_name='newuserModel',
        ),
    ]
