# Generated by Django 3.0.7 on 2020-06-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0009_auto_20200626_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='english',
        ),
        migrations.RemoveField(
            model_name='books',
            name='hindi',
        ),
        migrations.RemoveField(
            model_name='books',
            name='maths',
        ),
        migrations.RemoveField(
            model_name='books',
            name='most_selled',
        ),
        migrations.RemoveField(
            model_name='books',
            name='new',
        ),
        migrations.RemoveField(
            model_name='books',
            name='science',
        ),
        migrations.RemoveField(
            model_name='books',
            name='social_studies',
        ),
        migrations.RemoveField(
            model_name='books',
            name='toprated',
        ),
        migrations.AddField(
            model_name='books',
            name='EMAIL',
            field=models.EmailField(default='raj079284@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='books',
            name='author_descriptions',
            field=models.TextField(default='oops! no data is available'),
        ),
        migrations.AddField(
            model_name='books',
            name='awards',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.CharField(default='unknown', max_length=150),
        ),
        migrations.AddField(
            model_name='books',
            name='book_description',
            field=models.TextField(default='oops! no data is available'),
        ),
        migrations.AddField(
            model_name='books',
            name='review',
            field=models.TextField(default='oops! no data is available'),
        ),
        migrations.AddField(
            model_name='books',
            name='total_chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='books',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
    ]
