# Generated by Django 5.0.1 on 2024-02-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_remove_xyz_abc_ptr_protfolio_slug_delete_asd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protfolio',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
