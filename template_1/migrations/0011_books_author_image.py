# Generated by Django 3.0.7 on 2020-06-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0010_auto_20200626_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author_image',
            field=models.ImageField(default='no_image_available.jpg', upload_to='author_image'),
        ),
    ]
