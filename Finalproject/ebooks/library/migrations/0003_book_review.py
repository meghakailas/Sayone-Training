# Generated by Django 2.0 on 2019-07-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
