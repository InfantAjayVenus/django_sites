# Generated by Django 4.1 on 2022-08-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=50)),
                ('full_url', models.URLField()),
                ('url_name', models.CharField(max_length=50)),
                ('short_url', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddConstraint(
            model_name='shorturl',
            constraint=models.UniqueConstraint(fields=('account_name', 'url_name'), name='unique_url'),
        ),
    ]