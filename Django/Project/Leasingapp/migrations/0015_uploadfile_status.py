# Generated by Django 4.1.2 on 2022-10-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leasingapp', '0014_adder_alter_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
