# Generated by Django 3.2.18 on 2023-03-25 18:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postgallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.RemoveField(
            model_name='postgallery',
            name='images',
        ),
        migrations.AddField(
            model_name='postgallery',
            name='images',
            field=models.ManyToManyField(related_name='gallery_images', to='blog.Image'),
        ),
    ]