# Generated by Django 4.1.3 on 2023-02-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг книги'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='author_rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг автора.'),
        ),
    ]