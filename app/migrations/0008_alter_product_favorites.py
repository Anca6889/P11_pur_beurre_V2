# Generated by Django 3.2.4 on 2021-07-12 08:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_alter_product_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(
                related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
