# Generated by Django 4.2.13 on 2024-06-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backgroundcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
    ]