# Generated by Django 3.2.12 on 2022-03-23 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0003_alter_events_prepare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='book',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
