# Generated by Django 4.2.6 on 2023-11-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=40)),
                ('PhoneNo', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
                ('type', models.IntegerField()),
            ],
        ),
    ]
