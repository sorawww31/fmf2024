# Generated by Django 4.2.8 on 2023-12-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudioTable', '0002_studiotable_date_alter_studiotable_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studiotable',
            name='weekday',
        ),
        migrations.AlterField(
            model_name='reservetable',
            name='period',
            field=models.CharField(max_length=5),
        ),
    ]
