# Generated by Django 4.1.2 on 2022-10-29 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leasingapp', '0010_rename_lessor_adder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adder',
        ),
    ]
