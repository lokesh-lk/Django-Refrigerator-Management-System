# Generated by Django 3.2.3 on 2021-06-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
