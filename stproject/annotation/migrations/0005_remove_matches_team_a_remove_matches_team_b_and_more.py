# Generated by Django 5.0.2 on 2024-04-29 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='team_a',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='team_b',
        ),
        migrations.DeleteModel(
            name='TeamA',
        ),
        migrations.DeleteModel(
            name='Matches',
        ),
        migrations.DeleteModel(
            name='TeamB',
        ),
    ]
