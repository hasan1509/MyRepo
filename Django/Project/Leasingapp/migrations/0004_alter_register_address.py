# Generated by Django 4.1.2 on 2022-10-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leasingapp', '0003_rename_registerlesse_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Address',
            field=models.CharField(max_length=100),
        ),
    ]