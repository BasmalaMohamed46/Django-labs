# Generated by Django 3.2.9 on 2024-05-11 20:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0002_auto_20240511_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='book',
            name='views',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.DeleteModel(
            name='ISBN',
        ),
    ]
