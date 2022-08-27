# Generated by Django 4.1 on 2022-08-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_url', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shorturl',
            name='unique_url',
        ),
        migrations.AddConstraint(
            model_name='shorturl',
            constraint=models.UniqueConstraint(fields=('account_name', 'url_name'), name='unique_url_name'),
        ),
    ]
