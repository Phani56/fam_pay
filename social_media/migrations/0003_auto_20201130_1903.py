# Generated by Django 3.1.3 on 2020-11-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0002_auto_20201130_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoarchive',
            name='external_id',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
