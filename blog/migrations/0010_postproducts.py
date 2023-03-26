# Generated by Django 3.2.18 on 2023-03-26 11:40

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20230325_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Title_image')),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('images', models.ManyToManyField(related_name='Product_images', to='blog.Image')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
