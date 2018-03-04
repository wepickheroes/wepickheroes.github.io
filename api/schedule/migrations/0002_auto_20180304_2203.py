# Generated by Django 2.0 on 2018-03-04 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='away_team_score',
            new_name='team_1_score',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='home_team_score',
            new_name='team_2_score',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team',
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_played_as_team_1', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_played_as_team_2', to='teams.Team'),
        ),
    ]
