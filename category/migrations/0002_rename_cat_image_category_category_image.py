# Generated by Django 4.2.3 on 2024-02-13 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_image',
            new_name='category_image',
        ),
    ]
