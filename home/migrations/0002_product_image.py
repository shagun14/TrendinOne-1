# Generated by Django 3.1.2 on 2020-11-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='uploads/products/'),
        ),
    ]
