# Generated by Django 2.2 on 2019-03-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0003_auto_20190313_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='relativeItemsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='newusermodel',
            name='date_of_birth',
        ),
    ]