# Generated by Django 4.0.4 on 2022-04-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]