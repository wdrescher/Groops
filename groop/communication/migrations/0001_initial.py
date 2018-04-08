# Generated by Django 2.0.2 on 2018-04-08 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grouprides', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('f_ride', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='grouprides.Ride')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('friend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='f_user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='communication.Profile'),
        ),
    ]
