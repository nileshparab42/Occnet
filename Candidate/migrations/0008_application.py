# Generated by Django 4.0.1 on 2022-01-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0007_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('sr', models.BigAutoField(primary_key=True, serialize=False)),
                ('A_name', models.CharField(max_length=120)),
                ('A_qualification', models.CharField(max_length=120)),
                ('A_email', models.CharField(max_length=120)),
                ('Company', models.CharField(max_length=120)),
                ('Vacancy', models.CharField(max_length=120)),
            ],
        ),
    ]
