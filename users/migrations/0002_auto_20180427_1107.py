# Generated by Django 2.0.4 on 2018-04-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='FirstName',
            field=models.TextField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='customer',
            name='LastName',
            field=models.TextField(blank=True, max_length=40),
        ),
    ]
