# Generated by Django 3.0.7 on 2020-06-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0016_auto_20200627_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_file',
            field=models.FileField(default='no file', upload_to='pdfs'),
        ),
    ]