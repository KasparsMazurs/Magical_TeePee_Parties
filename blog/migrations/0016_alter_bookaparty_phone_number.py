# Generated by Django 3.2.18 on 2023-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20230404_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookaparty',
            name='phone_number',
            field=models.CharField(default='+353 ', max_length=50),
        ),
    ]
