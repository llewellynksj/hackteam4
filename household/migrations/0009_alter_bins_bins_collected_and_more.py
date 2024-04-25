# Generated by Django 5.0.4 on 2024-04-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0008_bins_bins_next_collected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bins',
            name='bins_collected',
            field=models.ManyToManyField(blank=True, related_name='bins_collected', to='household.bin'),
        ),
        migrations.AlterField(
            model_name='bins',
            name='bins_next_collected',
            field=models.ManyToManyField(blank=True, related_name='bins_next_collected', to='household.bin'),
        ),
    ]