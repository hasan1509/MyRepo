# Generated by Django 4.1.5 on 2023-01-05 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='Username',
        ),
    ]
