# Generated by Django 2.1.7 on 2019-03-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pineapple', '0004_auto_20190226_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_image'),
        ),
    ]
