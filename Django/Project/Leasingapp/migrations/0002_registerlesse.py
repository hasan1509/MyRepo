# Generated by Django 4.1.2 on 2022-10-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leasingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerlesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Address', models.CharField(max_length=50)),
                ('Days', models.CharField(max_length=15)),
                ('Mobile', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=50)),
                ('Aadhar', models.CharField(max_length=15)),
            ],
        ),
    ]
