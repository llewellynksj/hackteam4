# Generated by Django 5.0.4 on 2024-04-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0002_task_category_task_description_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('kitchen', 'Kitchen'), ('food', 'Food'), ('shop', 'Shop'), ('laundry', 'Laundry'), ('bins', 'Bins'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
