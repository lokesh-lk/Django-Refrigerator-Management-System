# Generated by Django 3.2.3 on 2021-05-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inward',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
