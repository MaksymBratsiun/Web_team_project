# Generated by Django 4.2.1 on 2023-05-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storageapp', '0005_alter_file_user_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user_file_name',
            field=models.CharField(max_length=255),
        ),
    ]
