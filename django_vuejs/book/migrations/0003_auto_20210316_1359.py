# Generated by Django 3.1.7 on 2021-03-16 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_leads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='libraries',
            new_name='library',
        ),
    ]
