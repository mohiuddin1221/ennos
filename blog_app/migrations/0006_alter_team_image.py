# Generated by Django 5.0.1 on 2024-01-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='static/assets/img/team_images/'),
        ),
    ]
