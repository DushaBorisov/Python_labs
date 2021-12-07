# Generated by Django 3.2.9 on 2021-12-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('university', models.CharField(max_length=20)),
                ('course_number', models.IntegerField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
