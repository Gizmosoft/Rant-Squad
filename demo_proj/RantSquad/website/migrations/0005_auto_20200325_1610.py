# Generated by Django 3.0.3 on 2020-03-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200325_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.TextField(max_length=20),
        ),
    ]
