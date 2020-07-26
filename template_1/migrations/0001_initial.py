# Generated by Django 3.0.7 on 2020-06-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='firstpage_main_book_of_week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_background', models.ImageField(upload_to='')),
                ('small_image', models.ImageField(upload_to='')),
                ('name_of_book', models.CharField(max_length=100)),
                ('features', models.TextField()),
                ('published_date', models.DateField()),
                ('name_of_author', models.CharField(max_length=100)),
                ('about_author', models.TextField()),
                ('review_of_book', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='firstpage_mainbackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='')),
                ('small_image_1', models.ImageField(upload_to='')),
                ('small_image_2', models.ImageField(upload_to='')),
                ('small_image_3', models.ImageField(upload_to='')),
                ('name_image_1', models.CharField(max_length=100)),
                ('name_image_2', models.CharField(max_length=100)),
                ('name_image_3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='firstpage_reccomended_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_book_1', models.ImageField(upload_to='')),
                ('name_book_1', models.ImageField(upload_to='')),
                ('image_book_2', models.ImageField(upload_to='')),
                ('name_book_2', models.ImageField(upload_to='')),
                ('image_book_3', models.ImageField(upload_to='')),
                ('name_book_3', models.ImageField(upload_to='')),
                ('image_book_4', models.ImageField(upload_to='')),
                ('name_book_4', models.ImageField(upload_to='')),
                ('image_book_5', models.ImageField(upload_to='')),
                ('name_book_5', models.ImageField(upload_to='')),
                ('image_book_6', models.ImageField(upload_to='')),
                ('name_book_6', models.ImageField(upload_to='')),
            ],
        ),
    ]