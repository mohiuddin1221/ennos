# Generated by Django 5.0.1 on 2024-02-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_abc_asd_xyz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xyz',
            name='abc_ptr',
        ),
        migrations.AddField(
            model_name='protfolio',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.DeleteModel(
            name='asd',
        ),
        migrations.DeleteModel(
            name='abc',
        ),
        migrations.DeleteModel(
            name='xyz',
        ),
    ]
