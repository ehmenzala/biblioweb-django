# Generated by Django 5.0 on 2024-01-16 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('surname', models.CharField(max_length=75)),
                ('gender', models.CharField(choices=[(None, 'Género'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=9)),
                ('avatar', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(db_default=models.Value('No description'))),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=125)),
                ('language', models.CharField(max_length=125)),
                ('org_language', models.CharField(max_length=125, verbose_name='orginal lanugage')),
                ('pub_year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('rating', models.IntegerField(db_default=models.Value(0))),
                ('description', models.TextField(db_default=models.Value('No description'))),
                ('blurb', models.TextField(db_default=models.Value('No blurb'))),
                ('authors', models.ManyToManyField(to='books.author')),
                ('genres', models.ManyToManyField(to='books.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=255, verbose_name='alt text')),
                ('path', models.FilePathField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]