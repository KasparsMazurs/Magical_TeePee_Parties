# Generated by Django 3.2.18 on 2023-04-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_bookaparty_additional_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookaparty',
            name='status',
        ),
        migrations.AddField(
            model_name='bookaparty',
            name='phone_number',
            field=models.CharField(default='Contact number', max_length=50),
        ),
    ]
