# Generated by Django 2.2.12 on 2023-11-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_salary', models.IntegerField()),
                ('designation', models.CharField(max_length=25)),
                ('place', models.CharField(max_length=25)),
            ],
        ),
    ]
