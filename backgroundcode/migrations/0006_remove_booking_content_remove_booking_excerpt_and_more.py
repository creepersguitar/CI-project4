# Generated by Django 4.2.13 on 2024-07-16 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backgroundcode', '0005_alter_profile_options_rename_user_profile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='content',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='title',
        ),
    ]
