# Generated by Django 3.2 on 2022-03-03 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('distance', models.PositiveSmallIntegerField(verbose_name='Расстояние')),
            ],
            options={
                'db_table': 'some_model',
                'ordering': ['-date'],
            },
        ),
    ]
