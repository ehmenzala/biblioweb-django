# Generated by Django 5.0 on 2024-01-20 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_cover_book_book_cover_alter_cover_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cover',
            old_name='path',
            new_name='image',
        ),
    ]