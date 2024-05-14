# Generated by Django 3.2.9 on 2024-05-11 22:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0003_auto_20240511_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_categories', to='Bookstore.book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]