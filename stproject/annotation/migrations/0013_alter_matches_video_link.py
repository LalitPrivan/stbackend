# Generated by Django 5.0.2 on 2024-06-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0012_matches_game_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='video_link',
            field=models.URLField(unique=True),
        ),
    ]