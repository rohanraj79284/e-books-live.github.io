# Generated by Django 3.0.7 on 2020-06-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_1', '0004_delete_just_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstpage_famous_novelist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstpage_main_book_of_week',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstpage_mainbackground',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstpage_news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstpage_reccomended_books',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
