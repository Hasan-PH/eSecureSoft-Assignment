# Generated by Django 3.1.7 on 2021-02-26 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0006_student_school_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Information.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Information.subject')),
            ],
        ),
    ]
