# Generated by Django 5.0.2 on 2024-05-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0020_alter_teama_game_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='teama',
            name='match_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamb',
            name='match_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
