# Generated by Django 3.2.3 on 2021-06-16 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_inward_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inward',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
