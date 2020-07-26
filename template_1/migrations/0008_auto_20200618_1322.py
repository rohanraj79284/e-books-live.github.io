# Generated by Django 3.0.7 on 2020-06-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0007_remove_books_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='english',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='hindi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='maths',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='most_selled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='science',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='social_studies',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='books',
            name='toprated',
            field=models.BooleanField(default=False),
        ),
    ]