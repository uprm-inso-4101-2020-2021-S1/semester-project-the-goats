# Generated by Django 3.1.2 on 2020-10-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.TimeField(null=True),
        ),
    ]
