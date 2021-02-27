# Generated by Django 3.1.7 on 2021-02-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, unique=True)),
                ('credit', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
