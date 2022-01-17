# Generated by Django 4.0.1 on 2022-01-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0004_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=300)),
                ('pimg', models.TextField()),
                ('banner', models.TextField()),
                ('vname', models.CharField(max_length=300)),
                ('hname', models.CharField(max_length=300)),
                ('hdesc', models.TextField()),
                ('srtdesc', models.TextField()),
                ('lngdesc', models.TextField()),
                ('itime', models.DateField()),
                ('emp1', models.CharField(max_length=120)),
                ('title1', models.CharField(max_length=120)),
                ('emp2', models.CharField(max_length=120)),
                ('title2', models.CharField(max_length=120)),
                ('emp3', models.CharField(max_length=120)),
                ('title3', models.CharField(max_length=120)),
                ('emp4', models.CharField(max_length=120)),
                ('title4', models.CharField(max_length=120)),
                ('emp5', models.CharField(max_length=120)),
                ('emp6', models.CharField(max_length=120)),
                ('title6', models.CharField(max_length=120)),
            ],
        ),
    ]
