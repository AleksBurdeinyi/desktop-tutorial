# Generated by Django 4.2.4 on 2023-09-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_registrationmod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmod',
            name='password1',
            field=models.CharField(max_length=128),
        ),
    ]