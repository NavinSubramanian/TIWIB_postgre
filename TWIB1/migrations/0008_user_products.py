# Generated by Django 3.2.13 on 2023-08-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWIB1', '0007_content_typ2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products',
            field=models.TextField(default='9999'),
        ),
    ]
