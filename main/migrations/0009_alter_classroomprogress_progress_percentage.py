# Generated by Django 5.0.2 on 2024-04-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_classroomprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomprogress',
            name='progress_percentage',
            field=models.FloatField(default=0.0),
        ),
    ]