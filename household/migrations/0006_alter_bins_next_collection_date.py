# Generated by Django 5.0.4 on 2024-04-24 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0005_bin_bins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bins',
            name='next_collection_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]