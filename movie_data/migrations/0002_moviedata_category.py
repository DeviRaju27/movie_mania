# Generated by Django 5.0.6 on 2024-06-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='category',
            field=models.CharField(default='drama', max_length=100),
        ),
    ]
