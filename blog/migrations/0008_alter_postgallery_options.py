# Generated by Django 3.2.18 on 2023-03-14 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_postgallery_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postgallery',
            options={'ordering': ['-created_on']},
        ),
    ]
