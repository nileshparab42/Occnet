# Generated by Django 4.0.1 on 2022-01-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0008_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='A_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='A_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='A_qualification',
            new_name='qualification',
        ),
    ]
