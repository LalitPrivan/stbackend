# Generated by Django 5.0.2 on 2024-05-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0007_remove_matches_team_a_players_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='team_a_players',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='team_b_players',
            field=models.JSONField(blank=True, null=True),
        ),
    ]