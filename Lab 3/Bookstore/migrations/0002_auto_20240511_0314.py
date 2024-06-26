# Generated by Django 3.2.9 on 2024-05-11 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=100)),
                ('isbn_number', models.CharField(max_length=13, unique=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Bookstore.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='Bookstore.Category'),
        ),
    ]
