# Generated by Django 3.0.3 on 2020-03-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registerform',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
