# Generated by Django 2.0.5 on 2018-05-22 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateTimeField(default=django.utils.timezone.now)),
                ('Deposit', models.BooleanField(default=False)),
                ('Deposit_Amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
