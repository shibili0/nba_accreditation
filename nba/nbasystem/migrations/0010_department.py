# Generated by Django 4.0.4 on 2022-05-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0009_course_alter_parent_fname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptcode', models.CharField(max_length=200, null=True)),
                ('deptname', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
