# Generated by Django 3.2.3 on 2021-06-20 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0038_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='author',
            new_name='user',
        ),
    ]