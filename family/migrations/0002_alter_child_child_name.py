# Generated by Django 5.0.4 on 2024-04-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_name',
            field=models.CharField(max_length=100),
        ),
    ]