# Generated by Django 2.1.7 on 2019-03-13 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190313_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='userprofile',
        ),
    ]
