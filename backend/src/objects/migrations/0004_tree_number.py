# Generated by Django 4.1.5 on 2023-02-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_alter_objects_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
