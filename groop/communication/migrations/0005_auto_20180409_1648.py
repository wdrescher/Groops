# Generated by Django 2.0.2 on 2018-04-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0004_auto_20180408_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
