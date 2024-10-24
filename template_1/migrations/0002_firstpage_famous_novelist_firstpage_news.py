# Generated by Django 3.0.7 on 2020-06-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='firstpage_famous_novelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_of_novelist', models.ImageField(upload_to='')),
                ('name_of_author', models.TextField()),
                ('description_of_novelist', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='firstpage_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_serial_number', models.IntegerField()),
                ('news_image', models.ImageField(upload_to='')),
                ('new_heading', models.TextField()),
                ('news_date', models.DateField()),
                ('new_writer', models.TextField()),
            ],
        ),
    ]
