# Generated by Django 3.2.9 on 2024-05-11 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0004_auto_20240512_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='book',
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
