# Generated by Django 2.1.7 on 2019-02-25 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pineapple', '0003_auto_20190226_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='datelastorder',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=12),
            preserve_default=False,
        ),
    ]
