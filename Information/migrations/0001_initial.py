# Generated by Django 3.1.7 on 2021-02-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, unique=True)),
                ('location', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('gender', models.TextField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, max_length=250, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('mobile', models.TextField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('activate', models.BooleanField(default=True)),
            ],
        ),
    ]
