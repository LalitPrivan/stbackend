# Generated by Django 5.0.2 on 2024-05-23 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0024_remove_teama_dr_loc_remove_teama_or_loc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teama',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='teamb',
            name='match_id',
        ),
    ]
