# Generated by Django 4.2.13 on 2024-07-16 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backgroundcode', '0004_customuser_alter_booking_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(default='example@example.com'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=274560901928406, max_length=15),
        ),
    ]