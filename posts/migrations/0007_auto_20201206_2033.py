# Generated by Django 3.1.2 on 2020-12-06 20:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20201121_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
